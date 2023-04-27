from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse


class Learned(models.Model):
    level = models.CharField(max_length=20, verbose_name="Уровень", blank=True)
    mark_as_done = models.CharField(max_length=20, )

    def __str__(self):
        return self.level


class Skill(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    about = models.TextField(blank=True, verbose_name='Описание')
    links = ArrayField(models.CharField(max_length=200), blank=True, verbose_name='Ссылки')
    shape = models.CharField(max_length=20, verbose_name='Форма', blank=True)
    information_type = models.CharField(max_length=20, verbose_name='Тип информации', blank=True)
    skill_level = models.ForeignKey(Learned, on_delete=models.CASCADE, blank=True,  null=True, verbose_name="Уровень изучения")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('skill', kwargs={'skill_id': self.pk})


class Relation(models.Model):
    parent = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='child', blank=True)
    child = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="parent", blank=True)
