from django.urls import path
from SSF_app.views.competition_home_view import home_view2

urlpatterns = [
    path('', home_view2, name='competition-home'),
]