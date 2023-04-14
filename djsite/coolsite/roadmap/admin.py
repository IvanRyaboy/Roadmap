from django.contrib import admin

from .models import *


class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'about', 'links')
    list_display_links = ('id', 'name')


admin.site.register(Skill, SkillAdmin)
