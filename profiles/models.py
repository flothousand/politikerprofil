from django.db import models

# Create your models here.
class Profiles(models.Model):
    nachname = models.CharField(max_length=100)
    vorname = models.TextField()
    rolle_lang = models.CharField(max_length=20)
    fraktion = models.TextField()
    redenanzahl = models.FilePathField(path="/img")
    redelaenge = models.TextField()
    img_path_profil = models.FilePathField(path="/img")
    wordone = models.TextField()
    wordtwo = models.TextField()
    wordthree = models.TextField()
    entschuldigt = models.TextField()