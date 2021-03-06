# Generated by Django 3.2.11 on 2022-01-22 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plenarprotokoll', '0005_auto_20220118_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='plenarprotokoll',
            name='datum',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plenarprotokoll',
            name='img_path_wordcloud',
            field=models.FilePathField(default=0, path='/img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plenarprotokoll',
            name='ort',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plenarprotokoll',
            name='sitzungsnr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plenarprotokoll',
            name='wahlperiode',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterModelTable(
            name='plenarprotokoll',
            table='plenarprotokoll',
        ),
    ]
