from django.urls import path
from .views import *


urlpatterns = [
    #fsdfsd
    path("category/", CategoryList.as_view(), name="category-list"),
    path("category/<int:pk>/", CategoryDetail.as_view(), name="category-detail"),
    path("contact/", ContactList.as_view(), name="contact-list"),
    path("contact/<int:pk>/", ContactDetail.as_view(), name="contact-detail"),
    path("establishment/", EstablishmentList.as_view(), name="establishment-list"),
    path("establishment/<int:pk>/", EstablishmentDetail.as_view(),  name="establishment-detail"),
    path('establishment/<str:address>/', EstablishmentSearchByAddress.as_view()),
    path('establishment/<int:category>/',EstablishmentSearchByCategory.as_view()),
    path('establishment/<str:name>/', EstablishmentSearchByName.as_view()),
    
]
