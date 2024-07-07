# 4. Run server to ensure it works. Check URL.

from rest_framework.routers import DefaultRouter
from SSF_app.views.scoring_view import Scoring_Result_ViewSet, Scoring_Lift_ViewSet

scoring_router = DefaultRouter()
scoring_router.register(r'Lifts', Scoring_Lift_ViewSet)
scoring_router.register(r'Results', Scoring_Result_ViewSet)



urlpatterns = scoring_router.urls