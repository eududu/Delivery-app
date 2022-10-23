from django.urls import include, path
from .views import StoreViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Store', StoreViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
