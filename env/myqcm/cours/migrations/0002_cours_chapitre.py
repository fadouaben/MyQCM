# Generated by Django 4.2.4 on 2023-08-18 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chapitre', '0002_chapitre_student_chapitre_teacher_score_utilisateur'),
        ('cours', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='chapitre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chapitre.chapitre'),
            preserve_default=False,
        ),
    ]
