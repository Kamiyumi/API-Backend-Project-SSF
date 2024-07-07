from django.urls import include, path

urlpatterns = [
    path('community/', include('SSF_app.urls.community')),
    path('competition/', include('SSF_app.urls.competition')),
    path('scoring/', include('SSF_app.urls.scoring')),
    path('serie/', include('SSF_app.urls.serie')),
    path('landing/', include('SSF_app.urls.landing_urls')),
    path('login/', include('SSF_app.urls.login_urls')),

]
