# Generated by Django 4.2 on 2023-04-17 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roadmap', '0005_learned_remove_skill_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='skill_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='roadmap.learned'),
        ),
    ]
