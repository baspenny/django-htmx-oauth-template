from django.urls import path
from app.views import generic


urlpatterns = [
    path('', generic.home, name='home'),
    path('logout/', generic.logout_user, name='logout'),
]
