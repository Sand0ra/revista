from django.urls import path
from .views import *


urlpatterns = [
    path('v1/users/', UserAPIList.as_view()),
    path('v1/login/', LoginView.as_view()),
    path("v1/organizations/<int:organization_id>/customers", OrganizationCustomers.as_view()),
    path('v1/clients/<int:id>', ClientsApiDetail.as_view())
]
