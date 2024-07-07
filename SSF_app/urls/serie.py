from django.urls import path
from SSF_app.views.serie_home_view import home_view4

urlpatterns = [
    path('', home_view4, name='series-home'),
]
