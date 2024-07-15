from . import views
from django.urls import path


urlpatterns = [
    path('', views.resources_part, name='resources'),
]
