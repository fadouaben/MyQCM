# Generated by Django 4.1.10 on 2023-09-12 15:42

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
                ('valeur', models.TextField()),
                ('niveau', models.IntegerField(default=6)),
                ('matiere', models.TextField(default='رياضبات')),
            ],
        ),
        migrations.CreateModel(
            name='SousSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.TextField()),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skills.skill')),
            ],
        ),
    ]