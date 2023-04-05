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
    relation = Relation.objects.filter(parent_id=skill_id)
    relation_2 = Relation.objects.filter(child_id=skill_id)
    r = 3
    skill_2 = Skill.objects.raw(
        "SELECT (SELECT roadmap_skill.name FROM roadmap_skill WHERE roadmap_skill.id IN (SELECT child_id FROM roadmap_relation WHERE parent_id = %i", r)

    context = {
        'skill': skill,
        'relation': relation,
        'relation_2': relation_2,
        'title': skill.name,
        'skill_2': skill_2
    }

    return render(request, 'roadmap/skill.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
