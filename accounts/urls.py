from django.urls import path
from .views import RegisterAPI
from . import views


urlpatterns = [
    # API endpoints Documentation
    path('', views.getRoutes),
    # API endpoints to get and create users
    path('getUsers/', views.getUsers, name='getUsers'),
    path('getUsers/<str:pk>', views.getUser, name='getUser'),
    path('createUser/', RegisterAPI.as_view(), name='createUser'),

]
