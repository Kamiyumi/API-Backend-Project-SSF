from django.db import models
from django.db.models import UniqueConstraint
from datetime import datetime
import re
from datetime import date
from django.forms import ValidationError
import uuid

#X
class Person(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    SOCIAL_SECURITY_NR_REGEX = r'^\d{6}-\d{4}$'
    person_id = models.CharField(primary_key=True, max_length=255, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=MALE)
    email = models.EmailField(max_length=320, blank=True)  # Default empty string
    social_security_nr = models.CharField(max_length=255, unique=True, help_text="YYMMDD-XXXX")  # Format: YYMMDD-XXXX

    def __str__(self):
        return f"Name: {self.first_name or ''}, {self.last_name or ''}, SSN: {self.social_security_nr}, Gender: {self.gender}, Email: {self.email}"
    
    def clean(self):
        super().clean()
        # Validate social_security_nr format
        if not re.match(self.SOCIAL_SECURITY_NR_REGEX, self.social_security_nr):
            raise ValidationError('Social security number must be in the format "YYMMDD-XXXX".')
        
        # Additional validation for the date part
        date_part = self.social_security_nr[:6]
        try:
            date.fromisoformat(f"20{date_part[:2]}-{date_part[2:4]}-{date_part[4:6]}")
        except ValueError:
            raise ValidationError('Invalid date in social security number.')

    def save(self, *args, **kwargs):
        self.full_clean()  # Ensures that clean method is called
        super().save(*args, **kwargs)
        
    @property
    def age(self):
        birth_date_str = self.social_security_nr[:6]  # Extract the first 6 characters
        try:
            # Convert YYMMDD to YYYYMMDD
            year = int(birth_date_str[:2])
            month = int(birth_date_str[2:4])
            day = int(birth_date_str[4:6])
            
            # Determine century
            current_year = date.today().year
            current_century = current_year // 100 * 100
            birth_year = current_century + year
            if birth_year > current_year:
                birth_year -= 100

            birth_date = date(birth_year, month, day)
            today = date.today()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            return age
        except ValueError:
            return None  # Return None for invalid dates
            
    @property
    def license_nrs(self):
        return [license.license_nr for license in self.lifterlicense_set.all()]
    


class Club(models.Model):
    club_nr = models.IntegerField(primary_key=True, unique=True)
    club_orgnr = models.IntegerField(unique=True)
    club_phone = models.CharField(max_length=255, blank=True)
    club_email = models.EmailField(max_length=320, blank=True)
    club_website = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=False)  # Defaults to inactive
    paid = models.BooleanField(default=False)  # Defaults to unpaid
    district = models.ForeignKey('District', on_delete=models.CASCADE, db_column='RF_nr')

    def __str__(self):
        return f"Name: {self.name}, ClubNr: {self.club_nr}, OrgNr: {self.club_orgnr}, District: {self.district}"

    def clean(self):
        super().clean()
        # Validate club_nr length
        if not (10000 <= self.club_nr <= 99999):
            raise ValidationError('Club number must be a 5-digit number between 10000 and 99999.')

        # Validate club_orgnr format
        if not isinstance(self.club_orgnr, int) or self.club_orgnr < 0:
            raise ValidationError('Organization number must be a positive integer.')

        # Validate club_phone format (e.g., assuming a simple numeric format for this example)
        if self.club_phone and not re.match(r'^\+?\d{10,15}$', self.club_phone):
            raise ValidationError('Phone number must be a valid format (e.g., +1234567890).')

        # Validate club_website format (simple URL validation)
        if self.club_website and not re.match(r'^(https?://)?[\w.-]+(\.[\w.-]+)+[/#?]?.*$', self.club_website):
            raise ValidationError('Website must be a valid URL.')
        
        if self.name and len(self.name) < 3:
            raise ValidationError('Club name must be at least 3 characters long.')

    def save(self, *args, **kwargs):
        self.full_clean()  # Ensures that clean method is called
        super().save(*args, **kwargs)
    
#X

class LifterLicense(models.Model):
    LICENSE_NR_REGEX = r'^[a-zA-Z]{2}\d{5}L$'

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('non-active', 'Non-active'),
        ('pending', 'Pending'),
    ]

    license_nr = models.CharField(max_length=255, unique=True, help_text="License number in the format 'initials' + '5 digits' + 'L' (e.g., cc12345L)")
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=255, 
        choices=STATUS_CHOICES, 
        default='pending'
    )
    requested = models.DateField(help_text="Date of request")
    terminates = models.DateField(null=True, blank=True, help_text="Date of license expiry/termination")
    activated_date = models.DateField(null=True, blank=True, help_text="Date of license activation")
    paid = models.BooleanField(default=False)
    para = models.BooleanField(default=False)
    ifn = models.BooleanField(default=False)
    club = models.ForeignKey('Club', on_delete=models.CASCADE)
    club_membership_date = models.DateField(help_text="Date of club membership", null=True, blank=True)
    requested_year = models.IntegerField(editable=False)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['person', 'license_nr', 'requested_year'], name='unique_license')
        ]

    def clean(self):
        # Validate license_nr format
        if not re.match(self.LICENSE_NR_REGEX, self.license_nr):
            raise ValidationError('License number must be in the format "initials" + "5 digits" + "L" (e.g., cc12345L).')

        # Validate activated_date
        if self.activated_date:
            if self.activated_date < self.requested:
                raise ValidationError('Activated date cannot be before the requested date.')
            if self.terminates and self.activated_date > self.terminates:
                raise ValidationError('Activated date cannot be after the termination date.')
    
    def save(self, *args, **kwargs):
        if not self.terminates and self.requested:
            self.terminates = self.requested.replace(month=12, day=31)
        self.requested_year = self.requested.year
        self.full_clean()  # This will call the clean method
        super().save(*args, **kwargs)

    @property
    def get_first_name(self):
        return self.person.first_name

    @property
    def get_last_name(self):
        return self.person.last_name

    @property
    def get_gender(self):
        return self.person.gender

    @property
    def social_security_nr(self):
        return self.person.social_security_nr

    def __str__(self):
        return (f"Lifter License: {self.license_nr}")

#X
class RefereeLicense(models.Model):
    REF_LICENSE_NR_REGEX = r'^[a-zA-Z]{2}\d{5}D$'
    REFEREE_CATEGORIES = [
        ('distriksdomare', 'Distriksdomare'),
        ('förbundsdomare', 'Förbundsdomare'),
        ('internationell domare kat 1', 'Internationell domare kat 1'),
        ('internationell domare kat 2', 'Internationell domare kat 2')
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('non-active', 'Non-active'),
        ('pending', 'Pending'),
    ]

    referee_license_nr = models.CharField(max_length=255)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    authority = models.CharField(max_length=255)
    referee_category = models.CharField(
        max_length=255, 
        choices=REFEREE_CATEGORIES, 
        default='Ej angivet'
    )
    status = models.CharField(
        max_length=255, 
        choices=STATUS_CHOICES, 
        default='pending'
    )
    requested = models.DateField(help_text="Date of request")
    terminates = models.DateField(null=True, blank=True, help_text="Date of license expiry/termination")
    activated_date = models.DateField(null=True, blank=True, help_text="Date of license activation")
    paid = models.BooleanField(default=False)
    club = models.ForeignKey('Club', on_delete=models.CASCADE)
    club_membership_date = models.DateField(help_text="Date of club membership", null=True, blank=True)
    requested_year = models.IntegerField(editable=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['person', 'referee_license_nr', 'requested_year'], name='unique_referee_license')
        ]

    def save(self, *args, **kwargs):
        if not self.terminates and self.requested:
            self.terminates = self.requested.replace(month=12, day=31)
        self.requested_year = self.requested.year
        super().save(*args, **kwargs)

    @property
    def get_first_name(self):
        return self.person.first_name

    @property
    def get_last_name(self):
        return self.person.last_name

    @property
    def get_social_security_nr(self):
        return self.person.social_security_nr

    def __str__(self):
        return (f"Referee License: {self.referee_license_nr}")
    
    
class District(models.Model):
    RF_nr = models.CharField(primary_key=True, max_length=255, unique=True)
    district_name = models.CharField(max_length=255)
    district_orgnr = models.IntegerField(unique=True)
    district_phone = models.CharField(max_length=255, blank=True)
    district_email = models.EmailField(max_length=320, blank=True)
    district_website = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"RF number: {self.RF_nr}, Name: {self.district_name}, OrgNr: {self.district_orgnr}"

#X
class Violation(models.Model):
    report_id = models.AutoField(primary_key=True)
    violation = models.CharField(max_length=255, blank=True, null=True)
    repeal_start = models.DateField()
    repeal_end = models.DateField()
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Report ID {self.report_id} - '{self.violation}' by {self.author_first_name} {self.author_last_name} " \
               f"from {self.repeal_start} to {self.repeal_end}, Description: {self.description}, " \
               f"Person: {self.person.person_id} - {self.person.first_name} {self.person.last_name}"

