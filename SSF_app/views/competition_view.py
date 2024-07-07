from rest_framework import viewsets
from SSF_app.models.Competition import *
from SSF_app.api.competition_serializers import *
from SSF_app.api.scoring_serializers import Scoring_Result_Serializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from SSF_app.filters import Filter_Upcoming_Competition, Filter_Past_Competition, Filter_Result_WeightClass_Age, Filter_Ranking_Date_Age_Gender
from django.utils.timezone import now


class Competition_Discipline_ViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = Competition_Discipline_Serializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('discipline')
   

class Competition_Age_Category_ViewSet(viewsets.ModelViewSet):
    queryset = AgeCategory.objects.all()
    serializer_class = Competition_Age_Category_Serializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('lower_limit_age')
    


class Competition_Weight_Class_ViewSet(viewsets.ModelViewSet):
    queryset = WeightClass.objects.all()
    serializer_class = Competition_Weight_Class_Serializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('lower_limit', 'gender')  # Default ordering
   

class Competition_Competition_Type_ViewSet(viewsets.ModelViewSet):
    queryset = CompetitionType.objects.all()
    serializer_class = Competition_Competition_Type_Serializer
    

class Competition_Competition_ViewSet(viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = Competition_Competition_Serializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('start', 'competition_category')  # Default ordering

class Competition_Qualifying_Weight_ViewSet(viewsets.ModelViewSet):
    queryset = QualifyingWeight.objects.all()
    serializer_class = Competition_Qualifying_Weight_Serializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('minimum','weight_class', 'age_category')

class Competition_Group_ViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = Competition_Group_Serializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('competition')  # Default ordering

class Competition_Referee_Assignment_ViewSet(viewsets.ModelViewSet):
    queryset = RefereeAssignment.objects.all()
    serializer_class = Competition_Referee_Assignment_Serializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('group')


############################################################################################################
#Filter Classes

#This class is used to display the list of upcoming competitions, filtering out the ones that have already passed using the start date
#3.1.1 Kommande tävlingar
class Competition_Upcoming_List_ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = Competition_Upcoming_List_Serializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = Filter_Upcoming_Competition

    def get_queryset(self):
        queryset = super().get_queryset()
        # Apply default filtering for upcoming competitions
        queryset = queryset.filter(start__gte=now())
        # Apply default ordering
        queryset = queryset.order_by('start')
        return queryset

#This class is used to display the details of the past competitions, filtering out the ones that are still upcoming using the start date
# 3.1.2.1 Genomförda tävlingar

class Competition_Past_List_ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = Competition_Past_List_Serializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = Filter_Past_Competition

    def get_queryset(self):
        queryset = super().get_queryset()
        # Apply default filtering for upcoming competitions
        queryset = queryset.filter(start__lt=now())
        # Apply default ordering
        queryset = queryset.order_by('start')
        return queryset

# 3.1.2.2 Genomförda tävlingar - Detalj
#This class is used to display the details of the past competitions, filtering out the ones that are still upcoming using the start date 
class Competition_Past_Results_Detail_ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = Competition_Past_Detail_Serializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = Filter_Past_Competition

    def get_queryset(self):
        queryset = super().get_queryset()
        # Apply default filtering for upcoming competitions
        queryset = queryset.filter(start__lt=now())
        # Apply default ordering
        queryset = queryset.order_by('start')
        return queryset
    

    
#3.1.3.1 Tävling

#This class is used to display the details of the upcoming competitions, filtering out the ones that have already passed using the start date

class Competition_Upcoming_Detail_ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = Competition_Upcoming_Detail_Serializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = Filter_Upcoming_Competition

    def get_queryset(self):
        queryset = super().get_queryset()
        # Apply default filtering for upcoming competitions
        queryset = queryset.filter(start__gt=now())
        # Apply default ordering
        queryset = queryset.order_by('start')
        return queryset
    
#3.1.3.2 Genomförda tävlingar - Resultat
    
class Competition_Past_Lifter_Result_ViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = Competition_Lifter_Result_Serializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = Filter_Result_WeightClass_Age

    def get_queryset(self):
        return Result.objects.filter(group__competition__start__lt=now()).order_by(
            'weight_class', 'age_category', 'placement'
        )

#3.1.4 Ranking  
class Competition_Ranking_ViewSet (viewsets.ReadOnlyModelViewSet):
    queryset = Result.objects.all()
    serializer_class = Scoring_Result_Serializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = Filter_Ranking_Date_Age_Gender 

    def get_queryset(self):
        return Result.objects.all().order_by(
            'group__competition__start', 'weight_class', 'age_category', 'placement'
        )
