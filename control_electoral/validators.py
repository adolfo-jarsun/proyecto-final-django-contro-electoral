from django.core.exceptions import ValidationError

def validar_no_negativo(value):
    if value < 0:
        raise ValidationError("El valor no puede ser negativo.")


def validar_limite_votos(value):
    if value > 1000:
        raise ValidationError("El número de votos es demasiado alto para una mesa.")