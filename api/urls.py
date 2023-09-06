from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.CompanyListCreateView.as_view(), name='company-list'),
    path('companies/<int:pk>/', views.CompanyRetrieveUpdateDeleteView.as_view(), name='comany-retrieve'),
]
