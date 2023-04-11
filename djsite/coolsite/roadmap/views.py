from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import *
from .utils import DataMixin
from .functions import *


def index(request):
    skills = Relation.objects.select_related('parent', 'child').all()
    mermaid_str = "graph LR;\n"
    for item in skills:
        mermaid_str += "{} --> {}\n".format(item.parent.name, item.child.name)
    for item in skills:
        mermaid_str += f"click {item.parent.name} \"{item.parent.get_absolute_url()}\"\n" \
                       f"click {item.child.name} \"{item.child.get_absolute_url()}\"\n"

    context = {
        'mermaid_str': mermaid_str,
        'title': "Главная страница"
    }

    return render(request, 'roadmap/index.html', context=context)


def skill(request, skill_id):
    skill_list = []
    parent_skill = []
    skill = get_object_or_404(Skill, pk=skill_id)
    childs = skill.parent.all()
    parents = skill.child.all()
    parent_skill = (dfs(skill, skill_list))

    context = {
        'skill': skill,
        'parents': parents,
        'childs': childs,
        'parent_skill': parent_skill,
        'title': skill.name,
    }

    return render(request, 'roadmap/skill.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
