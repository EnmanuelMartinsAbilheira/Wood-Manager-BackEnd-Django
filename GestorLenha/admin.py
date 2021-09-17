from django.contrib import admin
from GestorLenha.models import Encomenda, Config

# Register your models here.

class EncomendaAdmin(admin.ModelAdmin):
               pass
admin.site.register(Encomenda, EncomendaAdmin)


class ConfigAdmin(admin.ModelAdmin):
               pass
admin.site.register(Config, ConfigAdmin)
