from django.contrib.auth.views import LoginView
from django.db.models import Q
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
    mermaid_str = "graph LR;\n"
    relation_list = get_all_relations()
    skill = get_object_or_404(Skill, pk=skill_id)
    parents = get_all_parent_relations(skill)
    parents.append(skill.name)
    childs = get_all_child_relations(skill)
    childs.append(skill.name)
    mermaid_str += parents_mermaid(parents, relation_list)
    mermaid_str += childs_mermaid(childs, relation_list)

    context = {
        'skill': skill,
        'parents': parents,
        'mermaid_str': mermaid_str,
        'title': skill.name,
    }

    return render(request, 'roadmap/skill.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
