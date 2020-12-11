from django.urls import path
from . import views
app_name = 'App_Customer'

urlpatterns = [
    path('', views.main, name='customer-login'),
]
