from django.apps import AppConfig


class PlenarprotokollConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'plenarprotokoll'

class MetaprotokollConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'metaprotokoll'