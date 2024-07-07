# 3. Import competition_router in the competition_home_view
# 4. Run server to ensure it works. Check URL.

from rest_framework.routers import DefaultRouter
from SSF_app.views.competition_view import (
    Competition_Discipline_ViewSet, 
    Competition_Age_Category_ViewSet, 
    Competition_Weight_Class_ViewSet, 
    Competition_Competition_Type_ViewSet, 
    Competition_Competition_ViewSet, 
    Competition_Qualifying_Weight_ViewSet, 
    Competition_Group_ViewSet, 
    Competition_Referee_Assignment_ViewSet, 
    Competition_Upcoming_List_ViewSet, 
    Competition_Upcoming_Detail_ViewSet, 
    Competition_Past_List_ViewSet,
    Competition_Past_Results_Detail_ViewSet,
    Competition_Past_Lifter_Result_ViewSet,
    Competition_Ranking_ViewSet
    )



competition_router = DefaultRouter()
competition_router.register(r'age_categories', Competition_Age_Category_ViewSet)
competition_router.register(r'competition_types', Competition_Competition_Type_ViewSet)
competition_router.register(r'competitions', Competition_Competition_ViewSet)
competition_router.register(r'disciplines', Competition_Discipline_ViewSet)
competition_router.register(r'groups', Competition_Group_ViewSet)
competition_router.register(r'past_competitions', Competition_Past_List_ViewSet, basename='past-competitions')
competition_router.register(r'past_competition_results', Competition_Past_Results_Detail_ViewSet, basename='past-competition-results')
competition_router.register(r'past_lifter_results', Competition_Past_Lifter_Result_ViewSet, basename='past-lifter-results')
competition_router.register(r'qualifying_weights', Competition_Qualifying_Weight_ViewSet)
competition_router.register(r'rankings', Competition_Ranking_ViewSet, basename='rankings')
competition_router.register(r'referee_assignments', Competition_Referee_Assignment_ViewSet)
competition_router.register(r'upcoming_competition_detail', Competition_Upcoming_Detail_ViewSet, basename='upcoming-competition-detail')
competition_router.register(r'upcoming_competitions', Competition_Upcoming_List_ViewSet, basename='upcoming-competitions')
competition_router.register(r'weight_classes', Competition_Weight_Class_ViewSet)

urlpatterns = competition_router.urls