# Generated by Django 4.2 on 2023-04-13 11:57

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('about', models.TextField(blank=True, verbose_name='Описание')),
                ('priority', models.IntegerField(verbose_name='Приоритет')),
                ('links', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None, verbose_name='Ссылки')),
                ('mark', models.IntegerField(blank=True, verbose_name='Пустышка')),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='roadmap.skill')),
                ('parent', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='roadmap.skill')),
            ],
        ),
    ]
