from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse


class Skill(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    about = models.TextField(blank=True, verbose_name='Описание')
    priority = models.IntegerField(verbose_name='Приоритет')
    links = ArrayField(models.CharField(max_length=200), blank=True, verbose_name='Ссылки')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('skill', kwargs={'skill_id': self.pk})


class Relation(models.Model):
    parent = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='parent', blank=True)
    child = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="child", blank=True)
