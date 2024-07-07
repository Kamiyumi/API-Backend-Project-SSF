from rest_framework import serializers
from SSF_app.models import *
from SSF_app.api.competition_serializers import *
from SSF_app.api.community_serializers import *
from SSF_app.api.scoring_serializers import *
from django.db.models import Sum


class Series_Serie_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = '__all__'

class Series_Division_Serializer(serializers.ModelSerializer):
    series = serializers.PrimaryKeyRelatedField(queryset=Series.objects.all())

    class Meta:
        model = Division
        fields = '__all__'


class Series_Team_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'

# Edited to return round result scores for each team etc.
class Series_TeamNoSeries_Division_Serializer(serializers.ModelSerializer):
    round_results = serializers.SerializerMethodField()
    total_score = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['title', 'paid', 'club', 'round_results', 'total_score']

    def get_round_results(self, obj):
        round_results = RoundResult.objects.filter(team=obj)
        return Series_RoundScoring_Result_Serializer(round_results, many=True).data #Gör annan serializer

    def get_total_score(self, obj):
        total_score = RoundResult.objects.filter(team=obj).aggregate(total_score=Sum('score'))['total_score']
        return total_score if total_score else 0
        

class Series_Round_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Round
        fields = '__all__'


#---Preliminary round result serializer
class Series_RoundScoring_Result_Serializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    round = serializers.PrimaryKeyRelatedField(queryset=Round.objects.all())
    included_results = Scoring_Result_Serializer(many=True, required=False)

    class Meta:
        model = RoundResult
        fields = '__all__'



#3.1.5 Lista över pågående serier
class Series_Current_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ['title', 'series_type', 'year']

#3.1.5 Möjlighet att se resultat från tidigare års serier som samlas under arkiv 

class Series_Past_Serializer(serializers.ModelSerializer):
    results = serializers.SerializerMethodField()

    class Meta:
        model = Series
        fields = ['title', 'series_type', 'year', 'results']

    def get_results(self, obj):
        # Get all divisions in the series
        divisions = obj.division_set.all()
        
        # Get all rounds in those divisions
        rounds = Round.objects.filter(division__in=divisions)
        
        # Get all round results in those rounds
        round_results = RoundResult.objects.filter(round__in=rounds)
        
        # Get all results included in those round results
        results = Result.objects.filter(id__in=round_results.values('included_results'))
        
        return Scoring_Result_Serializer(results, many=True).data
    
#3.1.6 Series med kopplade divisioner

class Series_With_Divisions_Serializer(serializers.ModelSerializer):
    divisions = serializers.SerializerMethodField()

    class Meta:
        model = Series
        fields = ['title', 'series_type', 'year', 'divisions']

    def get_divisions(self, obj):
        divisions = obj.division_set.all()
        return Series_Division_Serializer(divisions, many=True).data
    
#3.1.6 Specifika divisioners information

class Series_Division_Detail_Serializer(serializers.ModelSerializer):
    teams = serializers.SerializerMethodField()

    class Meta:
        model = Division
        fields = ['title', 'teams', 'limit_teams', 'teams_moving_up', 'teams_moving_down']
    
    def get_teams(self, obj):
        teams = obj.team_set.all()
        return Series_TeamNoSeries_Division_Serializer(teams, many=True).data
    

#3.1.7 Divison - Aktuella lag INTE KLAR

""" class TeamDivisonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['title', 'paid', 'club'] """