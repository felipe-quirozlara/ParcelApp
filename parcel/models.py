from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Envio(models.Model):
    name = models.CharField(max_length=100)
    fecha = models.DateTimeField(default=timezone.now)
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cliente', default=1)

    def __str__(self):
        return self.name

class Producto(models.Model):
    envio = models.ForeignKey(Envio, on_delete=models.PROTECT, default=1)
    nombre = models.CharField(max_length=250)
    peso = models.IntegerField()

    def __str__(self):
        return self.nombre + ' ' + str(self.envio)

class DireccionEnvio(models.Model):
    envio = models.ForeignKey(Envio, on_delete=models.CASCADE)
    calle = models.CharField(max_length=250)
    comuna = models.CharField(max_length=100)

    def __str__(self):
        return str(self.envio.id + ' ' + self.id + '' + self.calle)

class Retiro(models.Model):
    envio = models.ForeignKey(Envio, on_delete=models.CASCADE)
    calle = models.CharField(max_length=250)
    comuna = models.CharField(max_length=100)

    def __str__(self):
        return str(self.envio.id + ' ' + self.id + '' + self.calle)

class ListaPrecio(models.Model):
    distancia = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return str(self.id + ' ' + self.precio)


