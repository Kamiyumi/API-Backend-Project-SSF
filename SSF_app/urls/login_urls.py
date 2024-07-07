from django.urls import path
from SSF_app.views.login_view import login_view

urlpatterns = [
    path('login/', login_view, name='login'),
    
]