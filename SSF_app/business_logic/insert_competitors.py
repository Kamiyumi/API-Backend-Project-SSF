from SSF_app.models import RoundResult, Result

def add_competitors_to_round_results(round_result_id, competitor_ids):
    """
    Add competitors to the included_results of a RoundResult and update the score.

    Args:
        round_result_id (int): The ID of the RoundResult to update.
        competitor_ids (list): A list of competitor IDs to add to the included_results.
    """
    try:
        round_result = RoundResult.objects.get(id=round_result_id)
    except RoundResult.DoesNotExist:
        raise ValueError("RoundResult not found")

    competitors = Result.objects.filter(id__in=competitor_ids)
    round_result.included_results.add(*competitors)
    round_result.update_score()  # Update the score after adding competitors
