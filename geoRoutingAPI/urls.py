"""geoRoutingAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path


from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from convAPI import views


# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'surface', views.SurfaceViewSet)
router.register(r'UAVrouteInput', views.UAVrouteInputViewSet)
router.register(r'UAVgetCARS', views.UAVgetCARS)


# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
urlpatterns = [
 
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('convAPI.urls')),
    path('convAPI/', include('convAPI.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]