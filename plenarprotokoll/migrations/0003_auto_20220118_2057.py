# Generated by Django 3.2.11 on 2022-01-18 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plenarprotokoll', '0002_rename_project_plenarprotokoll'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plenarprotokoll',
            old_name='description',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='plenarprotokoll',
            old_name='title',
            new_name='redner',
        ),
        migrations.RenameField(
            model_name='plenarprotokoll',
            old_name='technology',
            new_name='vorname',
        ),
    ]
