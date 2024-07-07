from rest_framework import serializers
from SSF_app.models import *
from SSF_app.api.competition_serializers import Competition_Competition_Serializer
from django.core.exceptions import ObjectDoesNotExist


class Community_Person_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def validate_social_security_nr(self, value):
        SOCIAL_SECURITY_NR_REGEX = r'^\d{6}-\d{4}$'
        if not re.match(SOCIAL_SECURITY_NR_REGEX, value):
            raise serializers.ValidationError('Social security number must be in the format "YYMMDD-XXXX".')
        return value

    def validate(self, data):
        # Example of cross-field validation
        if data['first_name'] == data['last_name']:
            raise serializers.ValidationError('First name and last name cannot be the same.')
        return data


class Community_District_Serializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class Community_Club_Serializer(serializers.ModelSerializer):
    district = Community_District_Serializer(read_only=True)
    district_id = serializers.PrimaryKeyRelatedField(queryset=District.objects.all(), source='district', write_only=True)

    class Meta:
        model = Club
        fields = '__all__'

    def validate_club_nr(self, value):
        if not (10000 <= value <= 99999):
            raise serializers.ValidationError('Club number must be a 5-digit number between 10000 and 99999.')
        return value

    def validate_club_orgnr(self, value):
        if not isinstance(value, int) or value < 0:
            raise serializers.ValidationError('Organization number must be a positive integer.')
        return value

    def validate_club_phone(self, value):
        if value and not re.match(r'^\+?\d{10,15}$', value):
            raise serializers.ValidationError('Phone number must be a valid format (e.g., +1234567890).')
        return value

    def validate_club_website(self, value):
        if value and not re.match(r'^(https?://)?[\w.-]+(\.[\w.-]+)+[/#?]?.*$', value):
            raise serializers.ValidationError('Website must be a valid URL.')
        return value

    def validate(self, data):
        # Cross-field validation example
        if 'name' in data and len(data['name']) < 3:
            raise serializers.ValidationError('Club name must be at least 3 characters long.')
        return data

class Community_Club_Low_Detail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'


class Community_Lifter_License_Serializer(serializers.ModelSerializer):
    class Meta:
        model = LifterLicense
        fields = '__all__'

    def validate_license_nr(self, value):
        LICENSE_NR_REGEX = r'^[a-zA-Z]{2}\d{5}L$'
        if not re.match(LICENSE_NR_REGEX, value):
            raise serializers.ValidationError('License number must be in the format "initials" + "5 digits" + "L" (e.g., cc12345L).')
        return value

    def validate_activated_date(self, value):
        requested_str = self.initial_data.get('requested')
        terminates_str = self.initial_data.get('terminates')
        
        requested = datetime.strptime(requested_str, '%Y-%m-%d').date() if requested_str else None
        terminates = datetime.strptime(terminates_str, '%Y-%m-%d').date() if terminates_str else None

        if requested and value < requested:
            raise serializers.ValidationError('Activated date cannot be before the requested date.')
        if terminates and value > terminates:
            raise serializers.ValidationError('Activated date cannot be after the termination date.')
        return value

    def validate(self, data):
        requested = data.get('requested')
        terminates = data.get('terminates')
        activated_date = data.get('activated_date')

        if activated_date and requested and activated_date < requested:
            raise serializers.ValidationError('Activated date cannot be before the requested date.')
        if activated_date and terminates and activated_date > terminates:
            raise serializers.ValidationError('Activated date cannot be after the termination date.')

        return data


class Community_Referee_License_Serializer(serializers.ModelSerializer):
    person = Community_Person_Serializer(read_only=True)
    person_id = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all(), source='person', write_only=True)
    club = Community_Club_Serializer(read_only=True)
    club_id = serializers.PrimaryKeyRelatedField(queryset=Club.objects.all(), source='club', write_only=True)
    judged_competitions = serializers.SerializerMethodField()
    number_of_missions = serializers.SerializerMethodField()

    class Meta:
        model = RefereeLicense
        fields = '__all__'

    def get_judged_competitions(self, obj):
        # Get all referee assignments for the referee license
        referee_assignments = RefereeAssignment.objects.filter(referee_license=obj)
        # Get all competition IDs from the referee assignments
        competition_ids = referee_assignments.values_list('group__competition_id', flat=True)
        # Filter competitions by these IDs
        competitions = Competition.objects.filter(id__in=competition_ids)
        return Competition_Competition_Serializer(competitions, many=True).data

    def get_number_of_missions(self, obj):
        return RefereeAssignment.objects.filter(referee_license=obj).count() 

    def validate_referee_license_nr(self, value):
        REF_LICENSE_NR_REGEX = r'^[a-zA-Z]{2}\d{5}D$'
        if not re.match(REF_LICENSE_NR_REGEX, value):
            raise serializers.ValidationError('License number must be in the format "initials" + "5 digits" + "D" (e.g., ab12345D).')
        return value

    def validate_activated_date(self, value):
        requested_str = self.initial_data.get('requested')
        terminates_str = self.initial_data.get('terminates')
        
        requested = datetime.strptime(requested_str, '%Y-%m-%d').date() if requested_str else None
        terminates = datetime.strptime(terminates_str, '%Y-%m-%d').date() if terminates_str else None

        if requested and value < requested:
            raise serializers.ValidationError('Activated date cannot be before the requested date.')
        if terminates and value > terminates:
            raise serializers.ValidationError('Activated date cannot be after the termination date.')
        return value

    def validate(self, data):
        errors = {}
        requested = data.get('requested')
        terminates = data.get('terminates')
        activated_date = data.get('activated_date')

        if activated_date and requested and isinstance(requested, str):
            requested = datetime.strptime(requested, '%Y-%m-%d').date()

        if activated_date and terminates and isinstance(terminates, str):
            terminates = datetime.strptime(terminates, '%Y-%m-%d').date()

        if activated_date and requested and activated_date < requested:
            errors['activated_date'] = 'Activated date cannot be before the requested date.'
        if activated_date and terminates and activated_date > terminates:
            errors['activated_date'] = 'Activated date cannot be after the termination date.'

        if errors:
            raise serializers.ValidationError(errors)

        return data


class Community_Violation_Serializer(serializers.ModelSerializer):
    person = Community_Person_Serializer(read_only=True)
    person_id = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all(), source='person', write_only=True, allow_null=True)

    class Meta:
        model = Violation
        fields = '__all__'



class Community_Club_List_Serializer(serializers.ModelSerializer):
    district_name = serializers.CharField(source='district.district_name', read_only=True)

    class Meta:
        model = Club
        fields = ['club_nr', 'club_orgnr', 'name', 'active', 'paid', 'district', 'district_name']


#3.1.9 Förening i detalj

class Community_Club_Lifter_License_Serializer(serializers.ModelSerializer):
    person = Community_Person_Serializer(read_only=True)
    class Meta:
        model = LifterLicense
        fields = ['license_nr', 'person']

class Community_Club_Referee_License_Serializer(serializers.ModelSerializer):
    person = Community_Person_Serializer(read_only=True)
    
    class Meta:
        model = RefereeLicense
        fields = ['referee_license_nr', 'person']

#3.1.9 Förening i detalj

class Community_Club_Detail_Serializer(serializers.ModelSerializer):
    district_name = serializers.SerializerMethodField()
    lifters = Community_Club_Lifter_License_Serializer(many=True, read_only=True, source='lifterlicense_set')
    referees = Community_Club_Referee_License_Serializer(many=True, read_only=True, source='refereelicense_set')
    number_of_lifters = serializers.SerializerMethodField()
    number_of_referees = serializers.SerializerMethodField()

    class Meta:
        model = Club
        fields = ['club_nr','name', 'district_name', 'club_phone', 'club_email', 
                  'club_website', 'club_orgnr', 'lifters', 'referees', 
                  'number_of_lifters', 'number_of_referees']

    def get_district_name(self, obj):
        return obj.district.district_name

    def get_number_of_lifters(self, obj):
        return obj.lifterlicense_set.count()
        
    def get_number_of_referees(self, obj):
        return obj.refereelicense_set.count()    

#3.1.10 Distrikt i detalj

class Community_District_Detail_Serializer(serializers.ModelSerializer):
    clubs = Community_Club_Low_Detail_Serializer(many=True, read_only=True, source='club_set')
    associated_referees = serializers.SerializerMethodField()

    class Meta:
        model = District
        fields = ['district_name', 'district_phone', 'district_email', 'district_website', 'district_orgnr', 'clubs', 'associated_referees']

    def get_associated_referees(self, obj):
        referees = RefereeLicense.objects.filter(club__district=obj)
        return Community_Club_Referee_License_Serializer(referees, many=True).data
    


#3.1.13 Information på lyftare

class Community_Person_Info_Serializer(serializers.ModelSerializer):
    age_category = serializers.SerializerMethodField()
    active_lifter_license = serializers.SerializerMethodField()
    active_referee_license = serializers.SerializerMethodField()
    lifter_licenses = serializers.SerializerMethodField()
    referee_licenses = serializers.SerializerMethodField()
    results = serializers.SerializerMethodField()


    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age_category', 'active_lifter_license', 'active_referee_license', 'lifter_licenses', 'referee_licenses', 'results']

    def get_age_category(self, obj):
        age = obj.age
        if age is None:
            return "Invalid birth date"
        try:
            age_categories = AgeCategory.objects.filter(lower_limit_age__lte=age, upper_limit_age__gte=age)
            if age_categories.exists():
                return [category.title for category in age_categories]  # Return all matching categories
            return "No matching age category"
        except ObjectDoesNotExist:
            return "Error: AgeCategory not found"
        except Exception as e:
            return f"Error: {str(e)}"

    def get_active_lifter_license(self, obj):
        return LifterLicense.objects.filter(person=obj, status="active").exists()

    def get_active_referee_license(self, obj):
        return RefereeLicense.objects.filter(person=obj, status="active").exists()

    def get_lifter_licenses(self, obj):
        lifter_licenses = LifterLicense.objects.filter(person=obj)
        return Community_Lifter_License_Request_Serializer(lifter_licenses, many=True).data

    def get_referee_licenses(self, obj):
        referee_licenses = RefereeLicense.objects.filter(person=obj)
        return Community_Referee_License_Request_Serializer(referee_licenses, many=True).data
    
    def get_results(self, obj):
        results = Result.objects.filter(license_nr__person=obj)
        return Community_Lifter_Result_List_Serializer(results, many=True).data

  
class Community_Lifter_License_Request_Serializer(serializers.ModelSerializer):
    club_name = serializers.CharField(source='club.name', read_only=True)

    class Meta:
        model = LifterLicense
        fields = ['license_nr', 'requested', 'activated_date', 'club_name']

class Community_Referee_License_Request_Serializer(serializers.ModelSerializer):
    club_name = serializers.CharField(source='club.name', read_only=True)

    class Meta:
        model = RefereeLicense
        fields = ['referee_license_nr', 'requested', 'activated_date', 'club_name']

class Community_Lifter_Result_List_Serializer(serializers.ModelSerializer):
    competition_name = serializers.CharField(source='group.competition.title')
    competition_type = serializers.CharField(source='group.competition.competition_type.competition_type_nickname')
    competition_date = serializers.DateField(source='group.competition.start')
    lifter_bodyweight = serializers.DecimalField(source='body_weight', max_digits=5, decimal_places=3)
    WILKS_score = serializers.SerializerMethodField()
    IPFGL_score = serializers.SerializerMethodField()
    DOTS_score = serializers.SerializerMethodField()

    class Meta:
        model = Result
        fields = [
            'competition_name', 'competition_type', 'competition_date',
            'lifter_bodyweight', 'squat', 'benchpress', 'deadlift',
            'total', 'WILKS_score', 'IPFGL_score', 'DOTS_score'
        ]

    def get_WILKS_score(self, obj):
        # Assuming gender is part of the LifterLicense model
        gender = obj.license_nr.person.gender
        return obj.WILKS_male_score if gender == 'male' else obj.WILKS_female_score

    def get_IPFGL_score(self, obj):
        gender = obj.license_nr.person.gender
        return obj.IPFGL_male_score if gender == 'male' else obj.IPFGL_female_score

    def get_DOTS_score(self, obj):
        gender = obj.license_nr.person.gender
        return obj.DOTS_male_score if gender == 'male' else obj.DOTS_female_score

