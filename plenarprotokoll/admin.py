from django.contrib import admin

# Register your models here.
from .models import Plenarprotokoll, Metaprotokoll

admin.site.register(Plenarprotokoll)
admin.site.register(Metaprotokoll)
