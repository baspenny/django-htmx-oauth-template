from django.urls import path
from app.views import client_views


urlpatterns = [
    path('client/', client_views.list, name='client_list'),
    path('client/<id>', client_views.detail, name='client_detail'),
]
