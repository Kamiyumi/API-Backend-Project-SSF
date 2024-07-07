# 2. import its home_view in the "competition.py"
# 3. Import competition_router in the competition_home_view
# 4. Run server to ensure it works. Check URL.

from rest_framework.routers import DefaultRouter
from SSF_app.views.serie_view import Series_Series_ViewSet, Series_Division_ViewSet, Series_Team_ViewSet, Series_Round_ViewSet, Series_RoundScoring_Result_ViewSet
from SSF_app.views.serie_view import Series_Current_Series_ViewSet, Series_Past_Series_ViewSet, Series_Division_List_ViewSet, Series_Division_Detail_ViewSet

serie_router = DefaultRouter()
serie_router.register(r'current_series', Series_Current_Series_ViewSet, basename='current-series')
serie_router.register(r'division_detail', Series_Division_Detail_ViewSet, basename='division-detail')
serie_router.register(r'divisions', Series_Division_ViewSet)
serie_router.register(r'past_series_results', Series_Past_Series_ViewSet, basename='past-series-results')
serie_router.register(r'round_results', Series_RoundScoring_Result_ViewSet)
serie_router.register(r'rounds', Series_Round_ViewSet)
serie_router.register(r'series', Series_Series_ViewSet)
serie_router.register(r'series_divisions', Series_Division_List_ViewSet, basename='series-divisions')
serie_router.register(r'teams', Series_Team_ViewSet)


#---Fredrik Test
from SSF_app.views.serie_view import Series_PreliminaryRoundResultsViewSet

serie_router.register(r'preliminary_round_results', Series_PreliminaryRoundResultsViewSet, basename='preliminary_round_results')



urlpatterns = serie_router.urls