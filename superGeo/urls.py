from django.urls import path
from . import views

urlpatterns = [
    path("", views.SuperGeo_view, name="supergeo_view"),
    path("download/", views.download, name="download")
]
