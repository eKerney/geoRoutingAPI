from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RouteModelLineView, UAVgeojsonViewSet, UAVgetCARS, RouteOutputPointsView

router= DefaultRouter()

router.register(prefix='UAVrouter', viewset=UAVgeojsonViewSet, basename="UAVroutes")
router.register(prefix='UAVgetCARS', viewset=UAVgetCARS, basename="UAVgetCARS")
router.register(prefix='CARSrouteLine', viewset=RouteModelLineView, basename="CARSrouteLine")
router.register(prefix='CARSpointOutput', viewset=RouteOutputPointsView, basename="CARSpointOutput")
router.register(prefix='CARS', viewset=RouteModelLineView, basename="CARS")

#router.register(prefix='testAPIview', viewset=testAPIview, basename="testAPIview")

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('UAVroute/', UAVrouteInputViews.as_view()),
#     path('UAVroute/<int:id>', UAVrouteInputViews.as_view())
# ]
