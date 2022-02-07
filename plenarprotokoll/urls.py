from django.urls import path
from . import views

urlpatterns = [
    path("/", views.plenarprotokoll_overview, name="plenarprotokoll_overview"),
    path("/<int:sitzungsnr>/", views.plenarprotokoll_index, name="plenarprotokoll_index"),
    path("/<int:sitzungsnr>/<int:pk>", views.plenarprotokoll_detail, name="plenarprotokoll_detail"),
]