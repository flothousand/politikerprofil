from django.urls import path
from . import views

urlpatterns = [
    path("", views.profiles_index, name="profiles_index"),
    path("<int:pk>/", views.profiles_detail, name="profiles_detail"),
]