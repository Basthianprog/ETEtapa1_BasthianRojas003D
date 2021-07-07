from django.db import models

# Create your models here.

class Registro(models.Model):
    numeroid = models.CharField(primary_key=True,max_length=9, verbose_name='Numero de identificacion')
    foto = models.ImageField(upload_to="fotos", null=True, verbose_name='Fotografia proveedor')
    nombreComp = models.CharField(max_length=70, verbose_name='Nombre completo')
    Direccion = models.CharField(max_length=200, verbose_name='Nombre completo')
    email = models.CharField(max_length=20 , verbose_name="Correo electronico")
    pais = models.CharField(max_length=20,verbose_name="Pais")
    contrasenna = models.CharField(max_length=8, verbose_name="Contraseña")

    def __str__(self):
        return self.nombreComp

class Telefono(models.Model):
    Tipo = models.CharField(primary_key=True, max_length=9, verbose_name="Numero de telefono")
    ttelefono = models.IntegerField(verbose_name="Numero")
    registro = models.ForeignKey(Registro, on_delete=models.CASCADE)

    def __str__(self):
        return self.telefono


class Moneda(models.Model):
    idm = models.CharField(primary_key=True, max_length=2, verbose_name="id moneda")
    moneda = models.CharField(max_length=20,verbose_name="Tipo de moneda")
    registro = models.ForeignKey(Registro, on_delete=models.CASCADE)

    def __str__(self):
        return self.moneda

