from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import *
from .utils import DataMixin


def index(request):
    skill = Skill.objects.all()

    context = {
        'skill': skill,
        'title': "Главная страница"
    }

    return render(request, 'roadmap/index.html', context=context)


def skill(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)
    childs = skill.parent.all()
    parents = skill.child.all()

    context = {
        'skill': skill,
        'parents': parents,
        'childs': childs,
        'title': skill.name,
    }

    return render(request, 'roadmap/skill.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
