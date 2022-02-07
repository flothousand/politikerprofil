from django.urls import path
from . import views

urlpatterns = [
    path("/", views.impressum_overview, name="impressum_overview"),
]