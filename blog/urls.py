from . import views
from django.urls import path

urlpatterns = [path("<slug:slug>", views.BlogView.as_view(), name="blog_view"), 
               path("about/", views.AboutViwe.as_view(), name="about_view")]

