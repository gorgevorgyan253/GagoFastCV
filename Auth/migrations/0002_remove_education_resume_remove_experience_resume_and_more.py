# Generated by Django 5.1.3 on 2024-11-24 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='language',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='resume',
        ),
        migrations.DeleteModel(
            name='Certification',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
