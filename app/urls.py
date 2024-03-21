from django.urls import path
from app.views import client_views, generic


urlpatterns = [
    path('', generic.home, name='home'),
    path('logout/', generic.logout_user, name='logout'),
    path('client/', client_views.list, name='client_list'),
    path('client/<id>', client_views.detail, name='client_detail'),
]
