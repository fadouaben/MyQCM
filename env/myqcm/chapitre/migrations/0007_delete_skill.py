# Generated by Django 4.1.10 on 2023-09-12 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0004_delete_sousskill'),
        ('chapitre', '0006_rename_skills_skill'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
