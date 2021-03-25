from django.urls import path
from . import views as portView

urlpatterns = [
    path("", portView.index, name="home"),
    path("about/", portView.about, name="about"),
    path("projects/", portView.projects, name="projects"),
    path("resume/", portView.resume, name="resume"),
    path("contact/", portView.contact, name="contact"),
    path("projects/None/", portView.noLink, name="None"),
    path("load_certi", portView.load_certi, name="load_certi"),
    path("load_pro", portView.load_pro, name="load_pro"),
]
