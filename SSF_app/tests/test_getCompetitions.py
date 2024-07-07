from django.test import TestCase
from SSF_app.models import Competition, Round, Division, Series, CompetitionType, District, Club, Person, LifterLicense, Result, Group, WeightClass, AgeCategory, Team, Discipline, RoundResult
from SSF_app.models.Serie import update_score_on_change
from SSF_app.business_logic.prel_results import get_competitions_for_round, get_eligible_competitors, get_top_competitors, get_score_field, calculate_team_score, calculate_preliminary_round_results
from SSF_app.business_logic.insert_competitors import add_competitors_to_round_results
from SSF_app.business_logic.utils import get_score_field, is_bench_only
import decimal
from datetime import datetime

class PreliminaryResultFunctionsTestCase(TestCase):
    def setUp(self):
        self.competition_type = CompetitionType.objects.create(
            competition_type_nickname='KSL',
            title='Klassisk styrkelyft',
            classic=True,
            para=False,
            ifn=False
        )

        self.discipline1 = Discipline.objects.create(discipline="Knäböj")
        self.discipline2 = Discipline.objects.create(discipline="Benchpress")
        self.discipline3 = Discipline.objects.create(discipline="Deadlift")

        self.competition_type.disciplines.add(self.discipline1, self.discipline2, self.discipline3)

        self.agecat = AgeCategory.objects.create(
            title="Senior",
            lower_limit_age=14.00,
            upper_limit_age=100.00
        )

        self.weightclass_male1 = WeightClass.objects.create(
            title="male1",
            upper_limit=85.0,
            lower_limit=80.0,
            start_date=datetime(year=2021, month=1, day=1),
            end_date=datetime(year=2025, month=5, day=5),
            gender="male"
        )

        self.weightclass_female1 = WeightClass.objects.create(
            title="female1",
            upper_limit=60.0,
            lower_limit=52.0,
            start_date=datetime(year=2021, month=1, day=1),
            end_date=datetime(year=2025, month=5, day=5),
            gender="female"
        )

        self.series = Series.objects.create(
            serie_id='Test Series',
            title='Test Series Title',
            series_type='Test Type',
            year=2024,
            scoring_system='WILKS',
            gender='male',
            competition_type_nickname=self.competition_type
        )

        self.series.age_categories.add(self.agecat)

        self.district = District.objects.create(
            RF_nr='RF123',
            district_name='Test District',
            district_orgnr=123456
        )

        self.club = Club.objects.create(
            club_nr=12341,
            club_orgnr=12345,
            name='Test Club',
            active=True,
            paid=True,
            district=self.district
        )

        self.club2 = Club.objects.create(
            club_nr=22412,
            club_orgnr=13345,
            name='Test Club2',
            active=True,
            paid=True,
            district=self.district
        )

        self.division = Division.objects.create(
            division_id='Test Division',
            title='Test Division Title',
            limit_teams=5,
            limit_team_members=10,
            series=self.series
        )

        self.round = Round.objects.create(
            start=datetime(year=2024, month=1, day=1),
            end=datetime(year=2024, month=1, day=31),
            division=self.division
        )

        self.competition_within_round = Competition.objects.create(
            title='Competition Within Round',
            competition_category='Category A',
            location='Test Location',
            description='Test Description',
            start=datetime(year=2024, month=1, day=10),
            end=datetime(year=2024, month=1, day=20),
            reg_deadline=datetime(year=2023, month=12, day=31),
            location_address='Test Address',
            contact_phone='1234567890',
            contact_email='test@example.com',
            contact_name='Test Contact',
            competition_type=self.competition_type,
            club_orgnr=self.club,
            district_orgnr=self.district,
            invitation=None,
            registration_open=True,
            live_stream=None
        )

        self.competition_outside_round = Competition.objects.create(
            title='Competition Outside Round',
            competition_category='Category B',
            location='Test Location',
            description='Test Description',
            start=datetime(year=2023, month=12, day=1),
            end=datetime(year=2023, month=12, day=15),
            reg_deadline=datetime(year=2023, month=11, day=30),
            location_address='Test Address',
            contact_phone='0987654321',
            contact_email='outside@example.com',
            contact_name='Outside Contact',
            competition_type=self.competition_type,
            club_orgnr=self.club,
            district_orgnr=self.district,
            invitation=None,
            registration_open=True,
            live_stream=None
        )

        self.group = Group.objects.create(
            title='Group 1',
            competition=self.competition_within_round
        )

        self.male_person1 = Person.objects.create(
            first_name="John",
            last_name="Doe",
            gender="male",
            email="",
            social_security_nr="970327-2222"
        )

        self.male_person2 = Person.objects.create(
            first_name="Johnny",
            last_name="Doesson",
            gender="male",
            email="",
            social_security_nr="970327-2232"
        )

        self.female_person1 = Person.objects.create(
            first_name="Johnina",
            last_name="Doesina",
            gender="female",
            email="",
            social_security_nr="970327-2422"
        )

        self.female_person2 = Person.objects.create(
            first_name="Johnanna",
            last_name="Doesanna",
            gender="female",
            email="",
            social_security_nr="970327-2522"
        )

        self.lifter_license_male1 = LifterLicense.objects.create(
            license_nr='JD12345L',
            person=self.male_person1,
            status='active',
            requested=datetime(year=2024, month=1, day=1),
            terminates=datetime(year=2024, month=12, day=31),
            activated_date=datetime(year=2024, month=1, day=1),
            paid=True,
            para=False,
            ifn=False,
            club=self.club,
            club_membership_date=datetime(year=2024, month=1, day=1)
        )

        self.lifter_license_male2 = LifterLicense.objects.create(
            license_nr='JD12445L',
            person=self.male_person2,
            status='active',
            requested=datetime(year=2024, month=1, day=1),
            terminates=datetime(year=2024, month=12, day=31),
            activated_date=datetime(year=2024, month=1, day=1),
            paid=True,
            para=False,
            ifn=False,
            club=self.club2,
            club_membership_date=datetime(year=2024, month=1, day=1)
        )

        self.lifter_license_female1 = LifterLicense.objects.create(
            license_nr='JD12355L',
            person=self.female_person1,
            status='active',
            requested=datetime(year=2024, month=1, day=1),
            terminates=datetime(year=2024, month=12, day=31),
            activated_date=datetime(year=2024, month=1, day=1),
            paid=True,
            para=False,
            ifn=False,
            club=self.club,
            club_membership_date=datetime(year=2024, month=1, day=1)
        )

        self.lifter_license_female2 = LifterLicense.objects.create(
            license_nr='JD11345L',
            person=self.female_person2,
            status='active',
            requested=datetime(year=2024, month=1, day=1),
            terminates=datetime(year=2024, month=12, day=31),
            activated_date=datetime(year=2024, month=1, day=1),
            paid=True,
            para=False,
            ifn=False,
            club=self.club2,
            club_membership_date=datetime(year=2024, month=1, day=1)
        )

        self.result_male1 = Result.objects.create(
            body_weight=75,
            date=datetime(year=2024, month=1, day=15),
            lot_nr=1,
            placement=1,
            group=self.group,
            license_nr=self.lifter_license_male1,
            weight_class=self.weightclass_male1,
            age_category=self.agecat,
            WILKS_male_score=400,
            WILKS_female_score=0,
            IPFGL_male_score=0,
            IPFGL_female_score=0,
            DOTS_male_score=0,
            DOTS_female_score=0
        )

        self.result_male2 = Result.objects.create(
            body_weight=75,
            date=datetime(year=2024, month=1, day=15),
            lot_nr=1,
            placement=1,
            group=self.group,
            license_nr=self.lifter_license_male2,
            weight_class=self.weightclass_male1,
            age_category=self.agecat,
            WILKS_male_score=260,
            WILKS_female_score=0,
            IPFGL_male_score=0,
            IPFGL_female_score=0,
            DOTS_male_score=0,
            DOTS_female_score=0
        )

        self.result_female1 = Result.objects.create(
            body_weight=75,
            date=datetime(year=2024, month=1, day=15),
            lot_nr=1,
            placement=1,
            group=self.group,
            license_nr=self.lifter_license_female1,
            weight_class=self.weightclass_female1,
            age_category=self.agecat,
            WILKS_male_score=300,
            WILKS_female_score=0,
            IPFGL_male_score=0,
            IPFGL_female_score=0,
            DOTS_male_score=0,
            DOTS_female_score=0
        )

        self.result_female2 = Result.objects.create(
            body_weight=75,
            date=datetime(year=2024, month=1, day=15),
            lot_nr=1,
            placement=1,
            group=self.group,
            license_nr=self.lifter_license_female2,
            weight_class=self.weightclass_female1,
            age_category=self.agecat,
            WILKS_male_score=250,
            WILKS_female_score=0,
            IPFGL_male_score=0,
            IPFGL_female_score=0,
            DOTS_male_score=0,
            DOTS_female_score=0
        )

        self.team1 = Team.objects.create(
            title='Test Team',
            paid=True,
            division=self.division,
            club=self.club
        )

        self.team2 = Team.objects.create(
            title='Test Team 2',
            paid=True,
            division=self.division,
            club=self.club2
        )

    def test_get_eligible_competitors(self):
        competitions = [self.competition_within_round]
        eligible_competitors = get_eligible_competitors(self.team1, competitions)
        self.assertIn(self.result_male1, eligible_competitors)

    def test_is_bench_only(self):
        self.assertFalse(is_bench_only(self.competition_type))

    def test_get_top_competitors(self):
        competitions = [self.competition_within_round]
        competitors = get_eligible_competitors(self.team1, competitions)
        score_field = get_score_field(self.series, False, 'male')
        top_competitors = get_top_competitors(competitors, self.division.limit_team_members, score_field)
        self.assertIn(self.result_male1, top_competitors)

    def test_calculate_team_score(self):
        competitions = [self.competition_within_round]
        total_points, top_competitors = calculate_team_score(self.team1, competitions)
        self.assertEqual(float(total_points), 700.0)
        self.assertIn(self.result_male1, top_competitors)

    def test_calculate_preliminary_round_results(self):
        preliminary_results = calculate_preliminary_round_results(self.round)
        team1_result = next(result for result in preliminary_results if result['team'] == self.team1)
        self.assertEqual(team1_result['score'], 700.0)
        self.assertIn(self.result_male1, team1_result['competitors'])

    def test_add_competitors_to_round_results(self):
        round_result = RoundResult.objects.create(team=self.team1, round=self.round, score=0)
        competitors = [self.result_male1.id]
        add_competitors_to_round_results(round_result.id, competitors)
        round_result.refresh_from_db()
        self.assertIn(self.result_male1, round_result.included_results.all())

    def test_update_score_on_change(self):
        round_result = RoundResult.objects.create(team=self.team1, round=self.round, score=0)
        round_result.included_results.add(self.result_male1)
        update_score_on_change(None, round_result, action='post_add')
        round_result.refresh_from_db()
        self.assertEqual(float(round_result.score), 400.0)