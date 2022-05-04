from django.urls import path
from . import views

urlpatterns = [
    path('', views.shortner, name="shortner"),
    path('<str:shortened_link>/', views.our_redirect, name="redirect")
]