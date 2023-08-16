from django.urls import path,include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register("categorys",CategoryViewSet)
router.register("contacts", ContactViewSet, "contacts")
router.register("establishments", EstablishmentViewSet, "establishments")


urlpatterns = [
    path("", include(router.urls)),
    path('establishment/<str:address>/', EstablishmentSearchByAddress.as_view()),
    path('establishment/<int:category>/',EstablishmentSearchByCategory.as_view()),
    path('establishment/<str:name>/', EstablishmentSearchByName.as_view()),
    
]
