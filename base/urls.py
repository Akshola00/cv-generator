from django.urls import path
from base import views
urlpatterns = [
    path("", views.accept, name='accept'),
    path("resume/<int:id>", views.resume, name='resume'),
    path("profile", views.profile, name='profile'),

]
