from django.urls import include, path
from SSF_app.routers.community_router import community_router
from SSF_app.routers.competition_router import competition_router
from SSF_app.routers.scoring_router import scoring_router
from SSF_app.routers.series_router import serie_router


urlpatterns = [
    path('api_community/', include(community_router.urls)),
    path('api_competition/', include(competition_router.urls)),
    path('api_scoring/', include(scoring_router.urls)),
    path('api_series/', include(serie_router.urls)),
]