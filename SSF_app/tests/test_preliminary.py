# tests.py
"""
from django.test import TestCase
from SSF_app.models import (
    Team, Round, RoundResult, Club, District, Division, Series, 
    CompetitionType, Competition, Discipline, Result, Person, LifterLicense, AgeCategory, WeightClass, Group
)
from SSF_app.prel_results import (
    get_eligible_competitors, get_top_competitors, calculate_team_score, 
    get_competitions_for_round, calculate_preliminary_round_results, update_round_result_score
)
from decimal import Decimal

class ModelMethodsTestCase(TestCase):
    def setUp(self):
        discipline1, created = Discipline.objects.get_or_create(discipline='Knäböj')
        discipline2, created = Discipline.objects.get_or_create(discipline='Bänkpress')
        discipline3, created = Discipline.objects.get_or_create(discipline='Deadlift')

        # Create weight class
        weight_class = WeightClass.objects.create(
            upper_limit=80.0,
            lower_limit=70.0,
            title='70-80kg',
            start_date='2023-01-01',
            end_date='2023-12-31',
            gender='male'
        )

        # Create age category
        age_category = AgeCategory.objects.create(
            title='Senior',
            lower_limit_age=18,
            upper_limit_age=40
        )

        # Create a CompetitionType instance
        self.competition_type = CompetitionType.objects.create(
            competition_type_nickname='Test Competition',
            title='Test Competition Title',
            classic=True,
            para=False,
            ifn=False
        )
        self.competition_type.disciplines.add(discipline1, discipline2, discipline3)
        self.competition_type.weightclasses.add(weight_class)

        # Create a Series instance
        self.series = Series.objects.create(
            serie_id='Test Series',
            title='Test Series Title',
            series_type='Test Type',
            year=2024,
            scoring_system='WILKS',
            gender='male',
            competition_type_nickname=self.competition_type
        )

        # Create a District instance
        self.district = District.objects.create(RF_nr='RF123', district_name='Test District', district_orgnr=123456)

        # Create a Club instance
        self.club = Club.objects.create(club_nr=1, club_orgnr=123456, name='Test Club', active=True, paid=True, district=self.district)

        # Create a Division instance
        self.division = Division.objects.create(
            division_id='Test Division',
            title='Test Division Title',
            limit_teams=5,
            limit_team_members=10,
            series=self.series
        )

        # Create a Team instance
        self.team = Team.objects.create(title='Test Team', club=self.club, division=self.division, paid=True)

        # Create a Round instance
        self.round = Round.objects.create(start='2024-01-01', end='2024-01-31', division=self.division)

        # Create a Person instance
        self.person = Person.objects.create(
            first_name='John',
            last_name='Doe',
            gender='male',
            email='johndoe@example.com',
            social_security_nr='19900101XXXX'
        )

        # Create a LifterLicense instance
        self.lifter_license = LifterLicense.objects.create(
            license_nr='JD12345L',
            person=self.person,
            status='active',
            requested='2024-01-01',
            terminates='2024-12-31',
            activated_date='2024-01-01',
            paid=True,
            para=False,
            ifn=False,
            club=self.club,
            club_membership_date='2024-01-01'
        )

        # Create a Competition instance
        self.competition = Competition.objects.create(
            title='Test Competition',
            competition_category='Category A',
            location='Test Location',
            description='Test Description',
            start='2024-01-01',
            end='2024-01-02',
            reg_deadline='2023-12-31',
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

        # Create a Group instance
        self.group = Group.objects.create(title='Test Group', competition=self.competition)

        # Create a Result instance
        self.result = Result.objects.create(
            body_weight=75,
            date='2024-01-15',
            lot_nr=1,
            placement=1,
            group=self.group,
            license_nr=self.lifter_license,
            weight_class=weight_class,
            age_category=age_category,
            WILKS_female_score=200,
            WILKS_male_score=300,
            IPFGL_male_score=250,
            IPFGL_female_score=220,
            DOTS_male_score=270,
            DOTS_female_score=230,
            WILKS_female_BP_score=150,
            WILKS_male_BP_score=160,
            IPFGL_male_BP_score=170,
            IPFGL_female_BP_score=180,
            DOTS_male_BP_score=190,
            DOTS_female_BP_score=200,
            squat=150,
            benchpress=100,
            deadlift=200,
            total=450
        )

        # Create or get a RoundResult instance
        self.round_result, created = RoundResult.objects.get_or_create(team=self.team, round=self.round, defaults={'score': 0})
        self.round_result.included_results.add(self.result)

    def test_get_eligible_competitors(self):
        competitions = [self.competition]
        competitors = get_eligible_competitors(self.team, competitions)
        self.assertTrue(competitors.exists())

    def test_get_top_competitors(self):
        competitions = [self.competition]
        competitors = get_eligible_competitors(self.team, competitions)
        top_competitors = get_top_competitors(competitors, self.division.limit_team_members)
        self.assertEqual(len(top_competitors), self.division.limit_team_members)

    def test_calculate_team_score(self):
        competitions = [self.competition]
        total_points, top_competitors = calculate_team_score(self.team, competitions)
        self.assertGreater(total_points, 0)

    def test_get_competitions_for_round(self):
        competitions = get_competitions_for_round(self.round)
        self.assertTrue(competitions.exists())

    def test_calculate_preliminary_round_results(self):
        preliminary_results = calculate_preliminary_round_results(self.round)
        self.assertTrue(preliminary_results)

    def test_update_score(self):
        update_round_result_score(self.round_result)
        self.assertEqual(self.round_result.score, Decimal('300.000000'))
"""