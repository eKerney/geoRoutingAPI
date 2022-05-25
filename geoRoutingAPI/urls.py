"""geoRoutingAPI URL Configuration
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
router.register(r'convAPI', views.RouteModelLineView)


# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
urlpatterns = [
 
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('convAPI.urls')),
    path('convAPI/', include('convAPI.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]