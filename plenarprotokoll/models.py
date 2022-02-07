from django.db import models

# Create your models here.
class Plenarprotokoll(models.Model):
    redner = models.TextField(blank = True, null = True )
    vorname = models.TextField(blank = True, null = True )
    nachname = models.TextField(blank = True, null = True )
    fraktion = models.TextField(blank = True, null = True )
    rolle_lang = models.TextField(blank = True, null = True )
    ort = models.TextField(blank = True, null = True )
    datum = models.TextField(blank = True, null = True )
    wahlperiode = models.TextField(blank = True, null = True )
    sitzungsnr = models.TextField(blank = True, null = True )
    img_path_wordcloud = models.FilePathField(path="/img")
    #id = models.IntegerField(blank = True, primary_key=True )
    class Meta:
    	db_table = "plenarprotokoll"

# Create your models here.
class Metaprotokoll(models.Model):
    ort = models.TextField(blank = True, null = True )
    datum = models.TextField(blank = True, null = True )
    wahlperiode = models.TextField(blank = True, null = True )
    sitzungsnr = models.TextField(blank = True, null = True )
    link = models.TextField(blank = True, null = True )
    id = models.IntegerField(blank = True, primary_key=True )
    path = models.FilePathField(path="/img")
    #img_path_wordcloud = models.FilePathField(path="/img")
    class Meta:
    	db_table = "meta"