from django.db import models

from .Community import Club
from .Scoring import Result
from .Competition import CompetitionType, AgeCategory
from SSF_app.business_logic.utils import is_bench_only, get_score_field

from decimal import Decimal
from django.db.models.signals import m2m_changed
from django.db import models
from django.dispatch import receiver


class Series(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    SCORING_SYSTEM_CHOICES = [
        ('WILKS', 'WILKS'),
        ('IPF2020', 'IPF2020'),
        ('IPFGL', 'IPFGL'),
        ('DOTS', 'DOTS'),
    ]
    
    serie_id = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    series_type = models.CharField(max_length=255)
    year = models.IntegerField()
    scoring_system = models.CharField(max_length=255, choices=SCORING_SYSTEM_CHOICES)
    gender = models.CharField(max_length=255,choices=GENDER_CHOICES, default=MALE)
    competition_type_nickname = models.ForeignKey(CompetitionType, on_delete=models.CASCADE, db_column='competition_type_nickname')
    age_categories = models.ManyToManyField(AgeCategory)

    def __str__(self):
        gender_info = f", Gender: {self.gender}" if self.gender else ""
        return f"{self.title} ({self.serie_id}), Year: {self.year}, Scoring System: {self.scoring_system}{gender_info}"

class Division(models.Model):
    # Fields for the Division model
    division_id = models.CharField(max_length=255, primary_key=True)    
    title = models.CharField(max_length=255)                           
    limit_teams = models.IntegerField()                                 
    limit_team_members = models.IntegerField()                          
    series = models.ForeignKey(Series, on_delete=models.CASCADE, db_column='serie_id')
    teams_moving_up = models.IntegerField(default=0)
    teams_moving_down = models.IntegerField(default=0)
    


    def __str__(self):
        return f"{self.title} (Division ID: {self.division_id}, Limit Teams: {self.limit_teams}, Limit Team Members: {self.limit_team_members})"

class Team(models.Model):

    title = models.CharField(max_length=255)                            
    paid = models.BooleanField(default=False)                           # Whether the team has paid
    division = models.ForeignKey(Division, on_delete=models.CASCADE)    
    club = models.ForeignKey(Club, on_delete=models.CASCADE, db_column='club_nr')  

    def __str__(self):
        return f"{self.title} - Paid: {'Yes' if self.paid else 'No'}, Division: {self.division.title}, Club: {self.club.name}"



class Round(models.Model):

    start = models.DateField()  
    end = models.DateField()
    division = models.ForeignKey(Division, on_delete=models.CASCADE)


    def __str__(self):
        return f"Round from {self.start} to {self.end} for {self.division.title}"



class RoundResult(models.Model):
    # Fields for the RoundResult model
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    included_results = models.ManyToManyField(Result)
    score = models.DecimalField(max_digits=10, decimal_places=6, default=Decimal('0.000000'), null=True)

    class Meta:
        unique_together = (('team', 'round'),)

    def __str__(self):
        return f"Team {self.team.team_id} in Round {self.round.round_id}"
    
    def update_score(self):
        """
        Update the score based on the included results.
        """
        gender = self.team.division.series.gender.lower()
        is_bench_press_only = is_bench_only(self.team.division.series.competition_type_nickname)
        score_field = get_score_field(self.team.division.series, is_bench_press_only, gender)
        
        self.score = sum(getattr(result, score_field) for result in self.included_results.all())
        self.save()

# Signal to update score when included_results changes
@receiver(m2m_changed, sender=RoundResult.included_results.through)
def update_score_on_change(sender, instance, **kwargs):
    if kwargs['action'] in ['post_add', 'post_remove', 'post_clear']:
        instance.update_score()

