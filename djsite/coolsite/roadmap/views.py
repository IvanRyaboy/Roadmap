from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .functions import *


def index(request):
    skills = Relation.objects.select_related('parent', 'child').all()
    mermaid_str = "graph LR;\n"
    for item in skills:
        mermaid_str += f"{item.parent.name}{item.parent.shape} --> {item.child.name}{item.child.shape}\n" \
                       f"click {item.parent.name} \"{item.parent.get_absolute_url()}\"\n" \
                       f"click {item.child.name} \"{item.child.get_absolute_url()}\"\n"

    context = {
        'mermaid_str': mermaid_str,
        'title': "Главная страница"
    }

    return render(request, 'roadmap/index.html', context=context)


def skill(request, skill_id):
    mermaid_str = "graph LR;\n"
    skills = Skill.objects.all()
    relation = relation_all()
    relation_list = get_all_relations(relation)
    skill = get_object_or_404(Skill, pk=skill_id)
    parents = get_all_parent_relations(skill)
    parents.append(skill.name)
    childs = get_all_child_relations(skill)
    childs.append(skill.name)
    mermaid_str += parents_childs_mermaid(parents, childs, relation_list, skills)

    context = {
        'skill': skill,
        'mermaid_str': mermaid_str,
        'title': skill.name,
    }

    return render(request, 'roadmap/skill.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
