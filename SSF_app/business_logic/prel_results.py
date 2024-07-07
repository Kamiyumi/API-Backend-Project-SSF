from SSF_app.models import Team, Result, Competition, Division
from SSF_app.business_logic.utils import is_bench_only, get_score_field
from django.db.models import Q

#X
def get_eligible_competitors(team, competitions):
    """
    Retrieve eligible competitors for a given team and competitions.

    Args:
        team (Team): The team for which to retrieve competitors.
        competitions (QuerySet): The competitions to consider.

    Returns:
        QuerySet: A queryset of eligible competitors for the team.
    """
    team_serie = team.division.series

    gender = team_serie.gender.lower()
    age_categories = team_serie.age_categories.all()
    age_category_ids = age_categories.values_list('title', flat=True)

    if gender == 'female' or gender == 'dam':
        return Result.objects.filter(
            group_competition_in=competitions,
            license_nr__club=team.club,
            license_nr__Person__gender='female' or 'dam',
            age_category__in=age_category_ids
        )
    else:
        return Result.objects.filter(
            group__competition__in=competitions,
            license_nr__club=team.club,
            age_category__in=age_category_ids
        )


def get_top_competitors(competitors, limit_team_members, score_field):
    order = '-' + score_field
    return competitors.order_by(order)[:limit_team_members]


def calculate_team_score(team, competitions):
    """
    Calculate the total score for a team based on eligible competitors.

    Args:
        team (Team): The team to calculate the score for.
        competitions (QuerySet): The competitions to consider.

    Returns:
        tuple: A tuple containing the total score and a queryset of the top competitors.
    """
    division = team.division
    serie = division.series
    is_bench_press_only = is_bench_only(serie.competition_type_nickname)
    gender = 'female' if serie.gender.lower() == ('female' or 'dam') else 'male'

    competitors = get_eligible_competitors(team, competitions)
    score_field = get_score_field(serie, is_bench_press_only=is_bench_press_only, gender=gender)
    top_competitors = get_top_competitors(competitors, division.limit_team_members, score_field=score_field)

    total_points = sum(getattr(competitor, score_field) for competitor in top_competitors)
    return total_points, top_competitors

#X
def get_competitions_for_round(round_obj):
    """
    Retrieve competitions that have the same competition type as the round's division series 
    and whose dates fall within (or overlap) the start and end dates of the round. Yet to be
    implemented is to match competitions on the condition "classic" or "non-classic".
    Args:
        round_obj (Round): The round object containing the date range and division information.

    Returns:
        QuerySet: A queryset of competitions that match the criteria.
    """
    competition_type = round_obj.division.series.competition_type_nickname

    return Competition.objects.filter(
        Q(start__lte=round_obj.end) &  # Competition starts on or before the round ends
        Q(end__gte=round_obj.start) &  # Competition ends on or after the round starts
        Q(competition_type=competition_type)  # Competition has the same type as the round's division series
    )


def calculate_preliminary_round_results(round_obj):
    """
    Calculate preliminary round results for a given round.

    This function calculates the preliminary results for all divisions within a series 
    based on the given round. It ensures that competitors are only assigned to one team 
    within the series. Yet to be implemented is that it also takes into consideration
    the competitors in the other rounds within the serie.

    Args:
        round_obj (Round): The round object for which to calculate preliminary results.

    Returns:
        list: A list of dictionaries containing the team, their score, and their competitors.
    """
    competitions = get_competitions_for_round(round_obj)
    divisions = Division.objects.filter(series=round_obj.division.series).order_by('-limit_team_members')
    preliminary_results = []
    assigned_competitors = set()  # Set to track assigned competitors

    for division in divisions:
        teams = Team.objects.filter(division=division)
        for team in teams:
            # Calculate the initial team score and competitors
            initial_team_score, team_competitors = calculate_team_score(team=team, competitions=competitions)

            # Filter out competitors already assigned to another team
            unique_team_competitors = [competitor for competitor in team_competitors if competitor.license_nr not in assigned_competitors]

            # Update the set of assigned competitors
            assigned_competitors.update(competitor.license_nr for competitor in unique_team_competitors)

            # Determine the score field again
            division = team.division
            serie = division.series
            is_bench_press_only = is_bench_only(serie.competition_type_nickname)
            gender = 'female' if serie.gender.lower() == ('female' or 'dam') else 'male'
            score_field = get_score_field(serie, is_bench_press_only=is_bench_press_only, gender=gender)

            # Recalculate the team score with the unique competitors
            team_score = sum(getattr(competitor, score_field) for competitor in unique_team_competitors)

            preliminary_results.append({
                'team': team,
                'score': team_score,
                'competitors': unique_team_competitors
            })

    return preliminary_results


