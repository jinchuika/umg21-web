from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=256)
    nit = models.CharField(max_length=12)
    telefono = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.nombre


class Vehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    marca = models.CharField(max_length=32)
    modelo = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.marca} - {self.modelo}'


class Servicio(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha = models.DateField()
    anotaciones = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.vehiculo} - {self.fecha}'
