"""
URL configuration for SSF project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import include, path
#from SSF_app.views import home_view, home_view2, home_view3, home_view4

#from SSF_app.views.community_home_view import community_router

#from SSF_app.views.competition_home_view import competition_router
#from SSF_app.views.scoring_home_view import scoring_router
#from SSF_app.views.serie_home_view import serie_router
#from django.shortcuts import redirect
#from django.conf import settings
#from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from SSF_app.views import home_view, home_view2, home_view3, home_view4
from SSF_app.routers import urlpatterns as api_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),
    path('home2/', home_view2 , name='home2'),
    path('home3/', home_view3 , name='home3'),
    path('home4/', home_view4 , name='home4'),
    path('', lambda request: redirect('home/', permanent=True)),
    path('api/', include(api_urlpatterns)),
    path('landing/', include('SSF_app.urls.landing_urls')),
    path('login/', include('SSF_app.urls.login_urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)