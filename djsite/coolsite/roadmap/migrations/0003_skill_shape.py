# Generated by Django 4.2 on 2023-04-13 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadmap', '0002_remove_skill_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='shape',
            field=models.CharField(blank=True, max_length=20, verbose_name='Форма'),
        ),
    ]
