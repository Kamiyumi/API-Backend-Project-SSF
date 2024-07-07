from rest_framework.routers import DefaultRouter
from SSF_app.views.community_view import (
    Community_Club_ViewSet,
    Community_District_ViewSet,
    Community_Lifter_License_ViewSet,
    Community_Person_ViewSet,
    Community_Referee_License_ViewSet,
    Community_Violation_ViewSet,
    Community_Filtered_Clubs_ViewSet, 
    Community_Detail_Clubs_ViewSet,
    Community_Detail_District_ViewSet,
    Community_Person_Information_ViewSet
)

# Register all routers here
community_router = DefaultRouter()
community_router.register(r'clubs', Community_Club_ViewSet, basename='clubs')
community_router.register(r'districts', Community_District_ViewSet)
community_router.register(r'lifterlicenses', Community_Lifter_License_ViewSet)
community_router.register(r'persons', Community_Person_ViewSet)
community_router.register(r'refereelicenses', Community_Referee_License_ViewSet)
community_router.register(r'violations', Community_Violation_ViewSet)
community_router.register(r'FilteredClub', Community_Filtered_Clubs_ViewSet, basename='FilteredClub')
community_router.register(r'ClubDetail', Community_Detail_Clubs_ViewSet, basename='ClubDetail')
community_router.register(r'DistrictDetail', Community_Detail_District_ViewSet, basename='DistrictDetail')
community_router.register(r'PersonInfo', Community_Person_Information_ViewSet, basename='PersonInfo')



