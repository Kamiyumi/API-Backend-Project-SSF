def is_bench_only(competition_type):
    disciplines = competition_type.disciplines.all()
    return disciplines.count() == 1 and (disciplines.filter(discipline__iexact='bänkpress').exists() or disciplines.filter(discipline__iexact='benchpress').exists())

def get_score_field(series, is_bench_press_only, gender):
    """
    Get the score field from a series, return the string representation.
    """
    if gender.lower() == 'herr':
        gender = 'male'
    if gender.lower() == 'dam':
        gender = 'female'
    return f"{series.scoring_system}_{gender}_BP_score" if is_bench_press_only else f"{series.scoring_system}_{gender}_score"