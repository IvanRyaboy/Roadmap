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


def relation_all():
    relation = Relation.objects.all()
    return relation


def get_all_relations(relation):
    paren_list = []
    child_list = []
    relation_list = []
    for i in range(len(relation)):
        paren_list.append(relation[i].parent.name)
        child_list.append(relation[i].child.name)
    for i in range(len(paren_list)):
        sublist = [paren_list[i], child_list[i]]
        relation_list.append(sublist)
    return relation_list


def parents_childs_mermaid(parents, childs, relation_list, skills):
    mermaid_str = ""
    for i in range(len(parents)):
        for j in range(len(parents)):
            if_list = [parents[i], parents[j]]
            if if_list in relation_list:
                mermaid_str += "{} --> {}\n".format(parents[i], parents[j])
                for s in skills:
                    if parents[i] == s.name:
                        mermaid_str += f"click {parents[i]} \"{s.get_absolute_url()}\"\n"
                    elif parents[j] == s.parent.name:
                        mermaid_str += f"click {parents[j]} \"{s.get_absolute_url()}\"\n"
    for i in range(len(childs)):
        for j in range(len(childs)):
            if_list = [childs[i], childs[j]]
            if if_list in relation_list:
                mermaid_str += "{} --> {}\n".format(childs[i], childs[j])
                for s in skills:
                    if childs[i] == s.name:
                        mermaid_str += f"click {childs[i]} \"{s.get_absolute_url()}\"\n"
                    elif childs[j] == s.name:
                        mermaid_str += f"click {childs[j]} \"{s.get_absolute_url()}\"\n"
    return mermaid_str
