from django.contrib import admin

# Register your models here.

from .models import (
    Departamento,
    Provincia,
    Municipio,
    AsientoElectoral,
    Circunscripcion,
    Recinto,
    Mesa
)


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "created", "updated")
    search_fields = ("nombre",)
    ordering = ("nombre",)


@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "departamento", "created", "updated")
    search_fields = ("nombre",)
    list_filter = ("departamento",)
    ordering = ("nombre",)


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "provincia", "created", "updated")
    search_fields = ("nombre",)
    list_filter = ("provincia",)
    ordering = ("nombre",)


@admin.register(AsientoElectoral)
class AsientoElectoralAdmin(admin.ModelAdmin):
    list_display = ("nombre", "municipio", "created", "updated")
    search_fields = ("nombre",)
    list_filter = ("municipio",)
    ordering = ("nombre",)


@admin.register(Circunscripcion)
class CircunscripcionAdmin(admin.ModelAdmin):
    list_display = ("numero", "tipo", "asiento", "created", "updated")
    search_fields = ("numero", "tipo")
    list_filter = ("tipo",)
    ordering = ("numero",)


@admin.register(Recinto)
class RecintoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "circunscripcion", "created", "updated")
    search_fields = ("nombre",)
    list_filter = ("circunscripcion",)
    ordering = ("nombre",)


@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    list_display = (
        "numero",
        "recinto",
        "estado",
        "votos_emitidos",
        "votos_validos",
        "created",
    )

    search_fields = ("numero", "recinto__nombre")
    list_filter = ("estado", "recinto__circunscripcion")

    ordering = ("numero",)

    # 🔥 esto es clave para navegar relaciones grandes
    autocomplete_fields = ("recinto",)