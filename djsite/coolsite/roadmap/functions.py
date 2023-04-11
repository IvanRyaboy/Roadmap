from .models import *


def dfs(skill, skill_list):
    skill_list.append(skill.name)
    for child_skill in skill.child.all():
        dfs(child_skill.parent, skill_list)
    return skill_list

