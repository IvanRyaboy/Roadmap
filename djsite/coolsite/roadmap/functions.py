from django.db.models import Q

from .models import *


def collect_parent_relations(skill, collected_relations):
    for relation in skill.parent.all():
        collected_relations.append(relation.parent.name)
        collect_parent_relations(relation.parent, collected_relations)


def get_all_parent_relations(skill):
    relations = []
    collect_parent_relations(skill, relations)
    return relations


def collect_child_relations(skill, collected_relations):
    for relation in skill.child.all():
        collected_relations.append(relation.child.name)
        collect_child_relations(relation.child, collected_relations)


def get_all_child_relations(skill):
    relations = []
    collect_child_relations(skill, relations)
    return relations


def get_all_relations():
    paren_list = []
    child_list = []
    relation_list = []
    relation = Relation.objects.all()
    for i in range(len(relation)):
        paren_list.append(relation[i].parent.name)
        child_list.append(relation[i].child.name)
    for i in range(len(paren_list)):
        sublist = [paren_list[i], child_list[i]]
        relation_list.append(sublist)
    return relation_list


def parents_mermaid(parents, relation_list):
    mermaid_str = ""
    for i in range(len(parents)):
        for j in range(len(parents)):
            if_list = [parents[i], parents[j]]
            if if_list in relation_list:
                mermaid_str += "{} --> {}\n".format(parents[i], parents[j])
    return mermaid_str


def childs_mermaid(childs, relation_list):
    mermaid_str = ""
    for i in range(len(childs)):
        for j in range(len(childs)):
            if_list = [childs[i], childs[j]]
            if if_list in relation_list:
                mermaid_str += "{} --> {}\n".format(childs[i], childs[j])
    return mermaid_str
