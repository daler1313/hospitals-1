from django.urls import path
from .views import CategoryList, CategoryDetail,ContactList,ContactDetail,HospitalList,HospitalDetail


urlpatterns = [
    #fsdfsd
    path("category/", CategoryList.as_view(), name="category-list"),
    path("category/<int:pk>/", CategoryDetail.as_view(), name="category-detail"),
    path("contact/", ContactList.as_view(), name="contact-list"),
    path("contact/<int:pk>/", ContactDetail.as_view(), name="contact-detail"),
    path("hospital/", HospitalList.as_view(), name="hospitalt-list"),
    path("hospital/<int:pk>/", HospitalDetail.as_view(), name="hospitalt-detail"),
]
