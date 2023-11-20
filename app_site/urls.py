from django.urls import path
from app_site import views

urlpatterns = [
    path('',views.index,name='index')
]
