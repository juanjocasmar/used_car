from django.db import models
from django.utils import timezone

# Create your models here.
class Vehiculo(models.Model):
    ESTADO_CHOICES = [
        ('Disponible', 'Disponible'),
        ('Vendido', 'Vendido')
    ]
    
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Disponible')

    def save(self, *args, **kwargs):
        if not self.precio_venta:
            self.precio_venta = self.precio_compra * 1.3  # 30% de ganancia
        super().save(*args, **kwargs)

    def utilidad(self):
        if self.precio_venta:
            return self.precio_venta - self.precio_compra
        return 0
    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio}) - {self.estado}"