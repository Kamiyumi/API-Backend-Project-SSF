from django.urls import path
from SSF_app.views.scoring_home_view import home_view3

urlpatterns = [
    path('', home_view3, name='scoring-home'),
]

