from rest_framework import serializers
from SSF_app.api.scoring_serializers import Scoring_Result_Serializer, Scoring_Lift_Serializer
from SSF_app.models import *

class Competition_Discipline_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'

class Competition_Age_Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AgeCategory
        fields = '__all__'

class Competition_Weight_Class_Serializer(serializers.ModelSerializer):
    class Meta:
        model = WeightClass
        fields = '__all__'

class Competition_Competition_Type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitionType
        fields = '__all__'

class Competition_Competition_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'

class Competition_Qualifying_Weight_Serializer(serializers.ModelSerializer):
    class Meta:
        model = QualifyingWeight
        fields = '__all__'

class Competition_Group_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class Competition_Referee_Assignment_Serializer(serializers.ModelSerializer):
    class Meta:
        model = RefereeAssignment
        fields = '__all__'
        
############################################################################################################

#3.1.1 Kommande tävlingar


class Competition_Upcoming_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ['title', 'competition_category', 'start']


class Competition_Past_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ['title', 'competition_category', 'start']


#Utifrån kravspecifikationen:
#3.1.2 Genomförda tävlingar

class Competition_Past_Detail_Serializer(serializers.ModelSerializer):
    results = serializers.SerializerMethodField()

    class Meta:
        model = Competition
        fields = ['title', 'competition_category', 'start', 'results']

    def get_results(self, obj):
        results = Result.objects.filter(group__competition=obj)
        return Scoring_Result_Serializer(results, many=True).data
    
#Utifrån kravspecifikationen:
#3.1.3 Tävling

class Competition_Upcoming_Detail_Serializer(serializers.ModelSerializer):
    is_registration_open = serializers.BooleanField(read_only=True)

    class Meta:
        model = Competition
        fields = [
            'id',
            'title',
            'competition_category',
            'location',
            'description',
            'start',
            'end',
            'reg_deadline',
            'location_address',
            'contact_phone',
            'contact_email',
            'contact_name',
            'competition_type',
            'club_orgnr',
            'district_orgnr',
            'invitation',
            'registration_open',
            'live_stream',
            'is_registration_open'
        ]

#Utifrån kravspecifikationen:
#3.1.3.2 Resultatlista för en lyftare

class Competition_Lifter_Result_Serializer(serializers.ModelSerializer):
    lifter_name = serializers.CharField(source='license_nr.person.first_name', read_only=True)
    lifter_club = serializers.CharField(source='license_nr.club.name', read_only=True)
    lifter_body_weight = serializers.DecimalField(source='body_weight', max_digits=5, decimal_places=3)
    lifts = Scoring_Lift_Serializer(many=True, read_only=True, source='lift_set')
    total_weight = serializers.DecimalField(source='total', max_digits=10, decimal_places=2)
    knäböj = serializers.DecimalField(source='squat', max_digits=5, decimal_places=2)
    bänkpress = serializers.DecimalField(source='benchpress', max_digits=5, decimal_places=2)
    marklyft = serializers.DecimalField(source='deadlift', max_digits=5, decimal_places=2)
    WILKS_score = serializers.SerializerMethodField()
    IPFGL_score = serializers.SerializerMethodField()
    DOTS_score = serializers.SerializerMethodField()
    weight_class = serializers.CharField(source='weight_class.title', read_only=True)
    age_category = serializers.CharField(source='age_category.title', read_only=True)

    class Meta:
        model = Result
        fields = [
            'placement',
            'lifter_name',
            'lifter_club',
            'lifter_body_weight',
            'weight_class',
            'age_category',
            'lifts',
            'knäböj',
            'bänkpress',
            'marklyft',
            'total_weight',
            'WILKS_score',
            'IPFGL_score',
            'DOTS_score'
        ]

    def get_WILKS_score(self, obj):
        if obj.license_nr.person.gender.lower() == 'male':
            return obj.WILKS_male_score
        else:
            return obj.WILKS_female_score

    def get_IPFGL_score(self, obj):
        if obj.license_nr.person.gender.lower() == 'male':
            return obj.IPFGL_male_score
        else:
            return obj.IPFGL_female_score

    def get_DOTS_score(self, obj):
        if obj.license_nr.person.gender.lower() == 'male':
            return obj.DOTS_male_score
        else:
            return obj.DOTS_female_score
        
