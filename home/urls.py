from django.urls import path
from . import views

urlpatterns = [
    # make sure names are unique so they easily can be referenced
    # in case the url changes
    path('', views.home, name='home-page'),
    path('employees/', views.employees, name="employee-page"),
    path('total_sales/', views.totalsales, name="total-sales-page"),
    path('carmodels', views.carmodels, name="car-models")
]
