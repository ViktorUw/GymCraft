# Generated by Django 5.0.3 on 2024-05-06 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0007_delete_trainingplans'),
        ('training_plans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomPlans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500, null=True)),
                ('exercises', models.ManyToManyField(to='exercises.exercises')),
            ],
        ),
    ]
