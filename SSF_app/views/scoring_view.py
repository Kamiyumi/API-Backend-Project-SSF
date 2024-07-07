from rest_framework import viewsets
from SSF_app.models.Scoring import Lift, Result
from django_filters.rest_framework import DjangoFilterBackend
from SSF_app.api.scoring_serializers import Scoring_Lift_Serializer, Scoring_Result_Serializer

class Scoring_Result_ViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all().order_by('date', 'weight_class', 'age_category')
    serializer_class = Scoring_Result_Serializer
    


class Scoring_Lift_ViewSet(viewsets.ModelViewSet):
    queryset = Lift.objects.all().order_by('result', 'discipline', 'try_nr')
    serializer_class = Scoring_Lift_Serializer
    




