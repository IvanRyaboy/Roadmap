from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('skill/<int:skill_id>', skill, name='skill')
]
