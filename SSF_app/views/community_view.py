from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from SSF_app.filters import Filter_Club_District_ClubName
from SSF_app.models.Community import Club, District, LifterLicense, Person, RefereeLicense, Violation
from SSF_app.api.community_serializers import (
    Community_Club_Serializer,
    Community_District_Serializer,
    Community_Lifter_License_Serializer,
    Community_Person_Serializer,
    Community_Referee_License_Serializer,
    Community_Violation_Serializer,
    Community_Club_List_Serializer,
    Community_Club_Detail_Serializer,
    Community_District_Detail_Serializer,
    Community_Person_Info_Serializer

)

class Community_Person_ViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    @action(detail=False, methods=['get'], url_path='search', url_name='search')
    def search(self, request):
        queryset = self.get_queryset()

        first_name = request.query_params.get('first_name')
        
        last_name = request.query_params.get('last_name')

        if first_name:
            queryset = queryset.filter(first_name__icontains=first_name)
        if last_name:
            queryset = queryset.filter(last_name__icontains=last_name)

        serializer = Community_Person_Serializer(queryset, many=True)
        return Response(serializer.data)
    
    serializer_class = Community_Person_Serializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('last_name', 'first_name')  # Default ordering

class Community_District_ViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = Community_District_Serializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('RF_nr')  # Default ordering

class Community_Club_ViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = Community_Club_Serializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('club_nr')


class Community_Lifter_License_ViewSet(viewsets.ModelViewSet):
    queryset = LifterLicense.objects.all()
    serializer_class = Community_Lifter_License_Serializer
   
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('license_nr')
    


class Community_Referee_License_ViewSet(viewsets.ModelViewSet):
    queryset = RefereeLicense.objects.all()
    serializer_class = Community_Referee_License_Serializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('referee_license_nr')

class Community_Violation_ViewSet(viewsets.ModelViewSet):
    queryset = Violation.objects.all()
    serializer_class = Community_Violation_Serializer

# Filtered Community_Club_ViewSet över distrikt

# 3.1.8 Föreningar

class Community_Filtered_Clubs_ViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = Community_Club_List_Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = Filter_Club_District_ClubName 
   


# 3.1.9 Förening

class Community_Detail_Clubs_ViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = Community_Club_Detail_Serializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('name')
    

# 3.1.10 Distrikt i detalj

class Community_Detail_District_ViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = Community_District_Detail_Serializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('district_name')

#3.1.13 Lyftarinformation

class Community_Person_Information_ViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = Community_Person_Info_Serializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('person_id')