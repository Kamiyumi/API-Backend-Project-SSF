from django.db import models
from django.db.models import OuterRef, Subquery, Max
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal
from django.core.exceptions import ValidationError

from .Community import LifterLicense
from .Competition import WeightClass, AgeCategory, Group, Discipline


from .score_math import *

class Result(models.Model):
    body_weight = models.DecimalField(max_digits=5, decimal_places=3)
    date = models.DateField()
    lot_nr = models.IntegerField()
    placement = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    license_nr = models.ForeignKey(LifterLicense, on_delete=models.CASCADE, db_column='license_nr')
    weight_class = models.ForeignKey(WeightClass, on_delete=models.CASCADE, db_column='weight_class_title')
    age_category = models.ForeignKey(AgeCategory, on_delete=models.CASCADE, db_column='age_category_title')
    

    WILKS_female_score = models.DecimalField(max_digits=10, decimal_places=6, default=Decimal('0.000000'))
    WILKS_male_score = models.DecimalField(max_digits=10, decimal_places=6, default=Decimal('0.000000'))
    IPFGL_male_score = models.DecimalField(max_digits=10, decimal_places=6, default=Decimal('0.000000'))
    IPFGL_female_score = models.DecimalField(max_digits=10, decimal_places=6, default=Decimal('0.000000'))
    DOTS_male_score = models.DecimalField(max_digits=10, decimal_places=6, default=Decimal('0.000000'))
    DOTS_female_score = models.DecimalField(max_digits=10, decimal_places=6, default=Decimal('0.000000'))

    WILKS_female_BP_score = models.DecimalField(max_digits=10, decimal_places=6, default=Decimal('0.000000'))
    WILKS_male_BP_score = models.DecimalField(max_digits=10, decimal_places=6, default=Decimal('0.000000'))
    IPFGL_male_BP_score = models.DecimalField(max_digits=10, decimal_places=6, default=Decimal('0.000000'))
    IPFGL_female_BP_score = models.DecimalField(max_digits=10, decimal_places=6, default=Decimal('0.000000'))
    DOTS_male_BP_score = models.DecimalField(max_digits=10, decimal_places=6, default=Decimal('0.000000'))
    DOTS_female_BP_score = models.DecimalField(max_digits=10, decimal_places=6, default=Decimal('0.000000'))

    squat = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'))
    benchpress = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'))
    deadlift = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'))
    total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"Result {self.placement} on {self.date}, Weight Class: {self.weight_class.title}, Age Category: {self.age_category.title}, Body Weight: {self.body_weight}"

    def calculate_scores(self):
        #self.para_female_BP_score = Decimal('0.000000')    
        #self.para_male_BP_score = Decimal('0.000000')      

        self.WILKS_female_score = Decimal('0.000000')
        self.WILKS_male_score = Decimal('0.000000')
        self.IPFGL_male_score = Decimal('0.000000')
        self.IPFGL_female_score = Decimal('0.000000')
        self.DOTS_male_score = Decimal('0.000000')
        self.DOTS_female_score = Decimal('0.000000')

        self.WILKS_female_BP_score = Decimal('0.000000')
        self.WILKS_male_BP_score = Decimal('0.000000')
        self.IPFGL_male_BP_score = Decimal('0.000000')
        self.IPFGL_female_BP_score = Decimal('0.000000')
        self.DOTS_male_BP_score = Decimal('0.000000')
        self.DOTS_female_BP_score = Decimal('0.000000')

        self.total_weight = Decimal('0.000')
        self.benchpress_weight = Decimal('0.000')

        self.squat = Decimal('0.00')
        self.benchpress = Decimal('0.00')
        self.deadlift = Decimal('0.00')
        self.total = Decimal('0.00')

        competition_type = self.group.competition.competition_type
        is_equipped = not competition_type.classic
        competition_disciplines = competition_type.disciplines.all()

        is_benchpress_only = competition_disciplines.count() == 1 and competition_disciplines.first().discipline.lower() in ['bänkpress', 'benchpress']

        max_weight_subquery = Lift.objects.filter(
            result=self,
            goodlift=True,
            discipline=OuterRef('discipline')
        ).values(
            'discipline'
        ).annotate(
            max_weight=Max('weight')
        ).values('max_weight')

        # Get the best lifts
        best_lifts = Lift.objects.filter(
            result=self,
            goodlift=True,
            weight=Subquery(max_weight_subquery)
        )

        for lift in best_lifts:
            discipline_name = lift.discipline.discipline.lower()
            if discipline_name in ["bänkpress", "benchpress"]:
                self.total_weight += lift.weight
                self.benchpress_weight = lift.weight
                self.benchpress = lift.weight
            elif discipline_name in ["squat", "knäböj"]:
                self.total_weight += lift.weight
                self.squat = lift.weight
            elif discipline_name in ["deadlift", "marklyft"]:
                self.total_weight += lift.weight
                self.deadlift = lift.weight

            self.total = self.squat + self.benchpress + self.deadlift

        if is_benchpress_only:
            self.WILKS_female_BP_score = wilks(False, self.body_weight, self.benchpress_weight)
            self.WILKS_male_BP_score = wilks(True, self.body_weight, self.benchpress_weight)
            self.IPFGL_male_BP_score = ipfgl(True, is_equipped, "B", self.body_weight, self.benchpress_weight)
            self.IPFGL_female_BP_score = ipfgl(False, is_equipped, "B", self.body_weight, self.benchpress_weight)
            self.DOTS_male_BP_score = dots(True, self.body_weight, self.benchpress_weight)
            self.DOTS_female_BP_score = dots(False, self.body_weight, self.benchpress_weight)
           
        else:
            self.WILKS_female_score = wilks(False, self.body_weight, self.total_weight)
            self.WILKS_male_score = wilks(True, self.body_weight, self.total_weight)
            self.IPFGL_male_score = ipfgl(True, is_equipped, "T", self.body_weight, self.total_weight)
            self.IPFGL_female_score = ipfgl(False, is_equipped, "T", self.body_weight, self.total_weight)
            self.DOTS_male_score = dots(True, self.body_weight, self.total_weight)
            self.DOTS_female_score = dots(False, self.body_weight, self.total_weight)

            self.WILKS_female_BP_score = wilks(False, self.body_weight, self.benchpress_weight)
            self.WILKS_male_BP_score = wilks(True, self.body_weight, self.benchpress_weight)
            self.IPFGL_male_BP_score = ipfgl(True, is_equipped, "B", self.body_weight, self.benchpress_weight)
            self.IPFGL_female_BP_score = ipfgl(False, is_equipped, "B", self.body_weight, self.benchpress_weight)
            self.DOTS_male_BP_score = dots(True, self.body_weight, self.benchpress_weight)
            self.DOTS_female_BP_score = dots(False, self.body_weight, self.benchpress_weight)

        self.save()


class Lift(models.Model):
    try_nr = models.IntegerField(editable=True)
    result = models.ForeignKey('Result', on_delete=models.CASCADE, db_column='result_id')
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, db_column='discipline')
    weight = models.DecimalField(max_digits=6, decimal_places=2)  # numeric(6, 2), 9999.99 kg
    goodlift = models.BooleanField()

    class Meta:
        unique_together = (('try_nr', 'result', 'discipline'),)  # Ensuring the combination is unique

    def __str__(self):
        return f"Try {self.try_nr}, Result ID: {self.result.id}, Discipline: {self.discipline.discipline}, Weight: {self.weight}, Goodlift: {self.goodlift,}, License Nr: {self.lifter_license_nr}"
    
    def validate(self):
        # Check for negative weight
        if self.weight < 0:
            raise ValidationError('Weight cannot be negative.')
        
        # Check for minimum weight
        if self.weight and self.weight < 20:
            raise ValidationError('Weight must be at least 20 kg.')

        # Check if there are previous lifts in the same discipline
        previous_lifts = self.get_previous_lifts()
        for previous_lift in previous_lifts:
            if self.weight <= previous_lift.weight:
                raise ValidationError('Weight for subsequent lift cannot be lower than or equal to any previous lift.')

    def get_previous_lifts(self):
        # Retrieve all previous lifts in the same discipline
        return Lift.objects.filter(
            result=self.result,
            discipline=self.discipline
        ).order_by('try_nr')

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set try_nr if this is a new instance
            previous_lifts = self.get_previous_lifts()
            if previous_lifts.exists():
                last_try_nr = previous_lifts.last().try_nr
                self.try_nr = last_try_nr + 1
            else:
                self.try_nr = 1
        
        # Call validate before saving the instance
        self.validate()
        super().save(*args, **kwargs)

@receiver(post_save, sender=Lift)
def update_result_scores(sender, instance, **kwargs):
    instance.result.calculate_scores()
