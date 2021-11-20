from django.db import models
from django.utils import timezone

CHOICES = [
    ('Agua', 'Agua'),
    ('Gas', 'Gas'),
    ('Internet', 'Internet'),
    ('Luz', 'Luz'),
]

CHOICES_TRX = [
    ('Tarjeta de Debito', 'Tarjeta de Debito'),
    ('Tarjeta de Credito', 'Tarjeta de Credito'),
    ('Efectivo', 'Efectivo'),
]

class Boleta(models.Model):
    codigo_barra = models.CharField(max_length=14, unique=True)
    tipo = models.CharField(max_length=8, choices=CHOICES, default='Agua')
    descripcion = models.CharField(max_length=50)
    fecha_vto = models.DateField('Fecha de Vencimiento')
    importe = models.DecimalField(max_digits=6,decimal_places=2)
    pago = models.BooleanField(default=False)

class Transaccion(models.Model):
    codigo_barra = models.CharField(max_length=14, unique=True)
    metodo = models.CharField(max_length=18, choices=CHOICES_TRX, default='Efectivo')
    numero_tarjeta = models.CharField(max_length=16, null=True, blank=True)
    importe = models.DecimalField(max_digits=6,decimal_places=2)
    fecha_pago = models.DateField(default=timezone.now)
