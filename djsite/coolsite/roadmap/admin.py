from django.contrib import admin

from .models import *


class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'about', 'priority', 'links')
    list_display_links = ('id', 'name')
    search_fields = ('priority', 'name')


admin.site.register(Skill, SkillAdmin)
