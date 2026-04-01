from django.db import models
from .validators import validar_no_negativo, validar_limite_votos


class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.CASCADE,
        related_name='provincias'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(
        Provincia,
        on_delete=models.CASCADE,
        related_name='municipios'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class AsientoElectoral(models.Model):
    nombre = models.CharField(max_length=150)
    municipio = models.ForeignKey(
        Municipio,
        on_delete=models.CASCADE,
        related_name='asientos'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Circunscripcion(models.Model):
    numero = models.CharField(max_length=20)
    tipo = models.CharField(max_length=50)
    asiento = models.ForeignKey(
        AsientoElectoral,
        on_delete=models.CASCADE,
        related_name='circunscripciones'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.numero} - {self.tipo}"


class Recinto(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.TextField(blank=True, null=True)
    circunscripcion = models.ForeignKey(
        Circunscripcion,
        on_delete=models.CASCADE,
        related_name='recintos'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


# 👇 ENUM para estado de mesa
class EstadoMesa(models.TextChoices):
    PRELIMINAR = 'PRE', 'Preliminar'
    CONSOLIDADO = 'CON', 'Consolidado'
    FINAL = 'FIN', 'Final'


class Mesa(models.Model):
    numero = models.IntegerField()
    recinto = models.ForeignKey(
        Recinto,
        on_delete=models.CASCADE,
        related_name='mesas'
    )

    # Estado de la mesa
    estado = models.CharField(
        max_length=3,
        choices=EstadoMesa.choices,
        default=EstadoMesa.PRELIMINAR
    )

    # Resultados
    candidato1 = models.IntegerField(
    default=0,
    validators=[validar_no_negativo, validar_limite_votos]
    )
    candidato2 = models.IntegerField(
    default=0,
    validators=[validar_no_negativo, validar_limite_votos]
    )
    candidato3 = models.IntegerField(
    default=0,
    validators=[validar_no_negativo, validar_limite_votos]
    )
    candidato4 = models.IntegerField(
    default=0,
    validators=[validar_no_negativo, validar_limite_votos]
    )
    candidato5 = models.IntegerField(
    default=0,
    validators=[validar_no_negativo, validar_limite_votos]
    )

    votantes_habilitados = models.IntegerField(default=0)
    votos_emitidos = models.IntegerField(default=0)
    votos_validos = models.IntegerField(default=0)
    votos_blancos = models.IntegerField(default=0)
    votos_nulos = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Mesa {self.numero} - {self.recinto.nombre}"