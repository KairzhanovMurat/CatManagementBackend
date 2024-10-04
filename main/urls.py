from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('cats', views.CatViewSet, basename='cats')
router.register('breeds', views.BreedViewSet, basename='breeds')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/rate/cats', views.CatRateView.as_view(), name='rate')
]
