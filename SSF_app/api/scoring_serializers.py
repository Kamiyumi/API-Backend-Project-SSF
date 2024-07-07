from rest_framework import serializers
from SSF_app.models import *
from SSF_app.api.competition_serializers import *
from SSF_app.api.community_serializers import *

#Testar poängräkning

class Scoring_Lift_Serializer(serializers.ModelSerializer):
    result = serializers.PrimaryKeyRelatedField(queryset=Result.objects.all())
    discipline = serializers.PrimaryKeyRelatedField(queryset=Discipline.objects.all())

    class Meta:
        model = Lift
        fields = '__all__'

class Scoring_Result_Serializer(serializers.ModelSerializer):
    group = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all())
    license_nr = serializers.PrimaryKeyRelatedField(queryset=LifterLicense.objects.all())
    weight_class = serializers.PrimaryKeyRelatedField(queryset=WeightClass.objects.all())
    age_category = serializers.PrimaryKeyRelatedField(queryset=AgeCategory.objects.all())
    lifts = Scoring_Lift_Serializer(many=True, read_only=True)

    class Meta:
        model = Result
        fields = '__all__'

