# Generated by Django 4.2 on 2023-04-17 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadmap', '0004_skill_information_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Learned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beginner', models.CharField(blank=True, max_length=20, verbose_name='Начальный')),
                ('average', models.CharField(blank=True, max_length=20, verbose_name='Средний')),
                ('advanced', models.CharField(blank=True, max_length=20, verbose_name='Продвинутый')),
            ],
        ),
        migrations.RemoveField(
            model_name='skill',
            name='priority',
        ),
    ]