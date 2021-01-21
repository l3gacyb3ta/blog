from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blog", views.post_list, name="blog"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("contact", views.contact, name="contact"),
    path("projects", views.projects, name="projects"),
]
