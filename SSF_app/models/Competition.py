from django.db import models

from django.utils import timezone
from django.core.exceptions import ValidationError
from decimal import Decimal



class Discipline(models.Model):
    discipline = models.CharField(max_length=255, primary_key=True, unique=True)

    def __str__(self):
        return self.discipline



class WeightClass(models.Model):
    #Gender choices male and female
    MALE = 'male'
    FEMALE = 'female'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    upper_limit = models.DecimalField(max_digits=5, decimal_places=2)
    lower_limit = models.DecimalField(max_digits=5, decimal_places=2)
    title = models.CharField(max_length=255, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, default=MALE)
    class Meta:
        unique_together = (('upper_limit', 'lower_limit', 'gender'),)

    def clean(self):
        super().clean()

        if self.start_date > self.end_date:
            raise ValidationError('Start date cannot be greater than end date.')

        # Validate lower_limit and upper_limit are within the logical range
        if not (30 <= self.lower_limit <= 120):
            raise ValidationError('Lower limit must be between 30 and 120.')
        if not (30 <= self.upper_limit <= 120):
            raise ValidationError('Upper limit must be between 30 and 120.')
        
        if (Decimal(self.upper_limit) - Decimal(self.lower_limit)) < 4:
            raise ValidationError('Difference between lower and upper limit must be at least 4.')

        # Ensure lower_limit is less than or equal to upper_limit
        if Decimal(self.lower_limit) >= Decimal(self.upper_limit):
            raise ValidationError('Lower limit cannot be equal or greater than upper limit.')

    def __str__(self):
        return f"Title: {self.title}, Gender: {self.gender}, Weight Range: {self.lower_limit}-{self.upper_limit}kg, Start Date: {self.start_date}, End Date: {self.end_date}"

    def save(self, *args, **kwargs):
        self.full_clean()  # This will call the clean method
        super().save(*args, **kwargs)



class AgeCategory(models.Model):
    title = models.CharField(max_length=255, primary_key=True)
    lower_limit_age = models.IntegerField()
    upper_limit_age = models.IntegerField()
    weightclasses = models.ManyToManyField(WeightClass)

    def __str__(self):
        return f"Title: {self.title}, Lower Limit Age: {self.lower_limit_age}, Upper Limit Age: {self.upper_limit_age}"


class CompetitionType(models.Model):
    competition_type_nickname = models.CharField(max_length=255, primary_key=True) #KSL
    title = models.CharField(max_length=255) #Klassisk styrkelyft
    classic = models.BooleanField(default=False)
    para = models.BooleanField(default=False)
    ifn = models.BooleanField(default=False)
    disciplines = models.ManyToManyField(Discipline)
    weightclasses = models.ManyToManyField(WeightClass)

    def __str__(self):
        return f"Nickname: {self.competition_type_nickname}, Title: {self.title}, Classic: {self.classic}, Para: {self.para}, IFN: {self.ifn}"


class Competition(models.Model):
    title = models.CharField(max_length=255)
    competition_category = models.CharField(max_length=255) #SM, DM
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    start = models.DateField()
    end = models.DateField()
    reg_deadline = models.DateField()
    location_address = models.CharField(max_length=255, blank=True)
    contact_phone = models.CharField(max_length=255, blank=True)
    contact_email = models.EmailField(max_length=255, blank=True)
    contact_name = models.CharField(max_length=255, blank=True)
    competition_type = models.ForeignKey('CompetitionType', on_delete=models.CASCADE)
    club_orgnr = models.ForeignKey('Club', on_delete=models.CASCADE, null=True)
    district_orgnr = models.ForeignKey('District', on_delete=models.CASCADE, null=True)
    invitation = models.FileField(upload_to='invitations/', blank=True, null=True)
    registration_open = models.BooleanField(default=False)
    live_stream = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def is_registration_open(self):
        return self.reg_deadline >= timezone.now().date()


class QualifyingWeight(models.Model):
    minimum = models.IntegerField()
    qualifying_period_start = models.DateField()
    qualifying_period_end = models.DateField()
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)                                      #Competition deletes
    age_category = models.ForeignKey(AgeCategory, on_delete=models.CASCADE, db_column='age_category_title')     #AgeCategory deletes
    weight_class = models.ForeignKey(WeightClass, on_delete=models.CASCADE, db_column='weight_class_title')     #WeightClass deletes

    def __str__(self):
        return f"Weight Class: {self.weight_class.title}, Age Category: {self.age_category.title}, Minimum: {self.minimum}, Qualifying Period Start: {self.qualifying_period_start}, Qualifying Period End: {self.qualifying_period_end}"


class Group(models.Model):
    title = models.CharField(max_length=255)
    speaker = models.CharField(max_length=255, blank=True, null=True)
    secretary = models.CharField(max_length=255, blank=True, null=True)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)      #Competition deletes

    
    def __str__(self):
        return f"Title: {self.title}"

class RefereeAssignment(models.Model):
    service = models.CharField(max_length=255, blank=True, null=True)
    referee_license = models.ForeignKey('RefereeLicense', on_delete=models.CASCADE)     #Referee deletes
    group = models.ForeignKey('Group', on_delete=models.CASCADE)                        #Group deletes

    def __str__(self):
        return f"Service: {self.service}, Referee License: {self.referee_license}, Group: {self.group}"


