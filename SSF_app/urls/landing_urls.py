from django.urls import path
from SSF_app.views.landing_views import föreningsadmin_landing_page, domaradmin_landing_page

urlpatterns = [
    path('föreningsadmin/', föreningsadmin_landing_page, name='föreningsadmin_landing'),
    path('domaradmin/', domaradmin_landing_page, name='domaradmin_landing')
]