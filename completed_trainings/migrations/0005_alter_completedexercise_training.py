# Generated by Django 5.0.3 on 2024-06-02 16:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('completed_trainings', '0004_remove_completed_training_exercises_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedexercise',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='completed_trainings.completed_training'),
        ),
    ]
