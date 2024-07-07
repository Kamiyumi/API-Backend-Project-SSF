from rest_framework import viewsets

from SSF_app.models.Serie import Series, Division, Team, Round, RoundResult
from SSF_app.api.Serie_serializers import *
from SSF_app.api.scoring_serializers import Scoring_Result_Serializer
from django.utils.timezone import now
from rest_framework.decorators import action
from SSF_app.business_logic.insert_competitors import add_competitors_to_round_results
from rest_framework.response import Response
from rest_framework import status


from SSF_app.business_logic.prel_results import *

class Series_Series_ViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = Series_Serie_Serializer

class Series_Division_ViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = Series_Division_Serializer

class Series_Team_ViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = Series_Team_Serializer

class Series_Round_ViewSet(viewsets.ModelViewSet):
    queryset = Round.objects.all()
    serializer_class = Series_Round_Serializer



class Series_RoundScoring_Result_ViewSet(viewsets.ModelViewSet):
    queryset = RoundResult.objects.all()
    serializer_class = Series_RoundScoring_Result_Serializer
    """
    Custom action to add competitors to a RoundResult.

    Args:
        request: The HTTP request object containing data.
        pk: The primary key of the RoundResult to update.

    Returns:
        Response: A DRF Response object containing the updated RoundResult or an error message.
    """
    @action(detail=True, methods=['post'])
    def add_competitors(self, request, pk=None):
        round_result_id = pk
        results_ids = request.data.get('results_ids', [])

        if not results_ids:
            return Response({'error': 'No result IDs provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Add competitors to the RoundResult
            add_competitors_to_round_results(round_result_id, results_ids)
            # Retrieve the updated RoundResult
            round_result = RoundResult.objects.get(id=round_result_id)
            # Serialize the updated RoundResult
            serializer = Series_RoundScoring_Result_Serializer(round_result)
            # Return the serialized data
            return Response(serializer.data, status=status.HTTP_200_OK)
        except RoundResult.DoesNotExist:
            return Response({'error': 'RoundResult not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['post'])
    def remove_competitors(self, request, pk=None):
        """
        Custom action to remove competitors from a RoundResult.

        Args:
            request: The HTTP request object containing data.
            pk: The primary key of the RoundResult to update.

        Returns:
            Response: A DRF Response object containing the updated RoundResult or an error message.
        """
        round_result_id = pk
        results_ids = request.data.get('results_ids', [])

        if not results_ids:
            return Response({'error': 'No result IDs provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Retrieve the RoundResult
            round_result = RoundResult.objects.get(id=round_result_id)
            # Filter the competitors to remove
            competitors_to_remove = Result.objects.filter(id__in=results_ids)
            # Remove the competitors from the included_results
            round_result.included_results.remove(*competitors_to_remove)
            # Update the score after removing competitors
            round_result.update_score()
            # Serialize the updated RoundResult
            serializer = Series_RoundScoring_Result_Serializer(round_result)
            # Return the serialized data
            return Response(serializer.data, status=status.HTTP_200_OK)
        except RoundResult.DoesNotExist:
            return Response({'error': 'RoundResult not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)





class Series_PreliminaryRoundResultsViewSet(viewsets.ViewSet):

    """
    Handle GET requests to list preliminary round results.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        Response: A DRF Response object containing the serialized preliminary results
                    or an error message.
    """
    def list(self, request):
        round_id = request.query_params.get('round_id')
        if not round_id:
            return Response({'error': 'round_id query parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            round_obj = Round.objects.get(id=round_id)
        except Round.DoesNotExist:
            return Response({'error': 'Round not found'}, status=status.HTTP_404_NOT_FOUND)

        preliminary_results = calculate_preliminary_round_results(round_obj)

        # Prepare the serialized results to be returned in the response
        serialized_results = []
        for result in preliminary_results:
            # serialize the data
            team_serializer = Series_Team_Serializer(result['team'])
            competitor_serializer = Scoring_Result_Serializer(result['competitors'], many=True)
            # Append the serialized data to the list
            serialized_results.append({
                'team': team_serializer.data,
                'score': result['score'],
                'competitors': competitor_serializer.data
            })

        return Response(serialized_results)



#3.1.5 Serier

class Series_Current_Series_ViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = Series_Current_Serializer

    def get_queryset(self):
        current_year = now().year
        return Series.objects.filter(year__gte=current_year)
    
#3.1.5 Serier - Möjlighet att se resultat från tidigare års serier som samlas under arkiv 

class Series_Past_Series_ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Series.objects.all()
    serializer_class = Series_Past_Serializer

    def get_queryset(self):
        current_year = now().year
        return Series.objects.filter(year__lt=current_year)
    
#3.1.6 Specifik serie  | Tabell med vilka divisioner som tillhör serien 

class Series_Division_List_ViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = Series_With_Divisions_Serializer


class Series_Division_Detail_ViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = Series_Division_Detail_Serializer

