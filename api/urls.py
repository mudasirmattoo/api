from django.urls import path
from .views import get_operation_code, process_data
from api import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bfhl', views.process_data, name='process_data'),
    path('bfhl', views.get_operation_code, name='get_operation_code'),
]
