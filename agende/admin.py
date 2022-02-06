from django.contrib import admin
from .models import agendamento, usuario, unidade
# Register your models here.


class UsuarioAdmin(admin.ModelAdmin):
    ...


class UnidadeAdmin(admin.ModelAdmin):
    ...


class AgendamentoAdmin(admin.ModelAdmin):
    ...


admin.site.register(usuario, UsuarioAdmin)

admin.site.register(unidade, UnidadeAdmin)

admin.site.register(agendamento, AgendamentoAdmin)
