from django.db import models

# Create your models here.

class Maestro(models.Model):
    nombre = models.CharField(max_length=255)
    matricula = models.CharField(max_length=20)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)

class Ejercicio(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    entrada_descripcion = models.TextField()
    salida_esperada_descripcion = models.TextField()
    entrada_ejemplo = models.TextField()
    salida_ejemplo = models.TextField()
    fecha_inicio = models.DateField()
    fecha_cierre = models.DateField()
    maestro = models.ForeignKey(Maestro, on_delete=models.CASCADE)

class CasoPrueba(models.Model):
    entrada = models.TextField()
    salida_esperada = models.TextField()
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)

class Alumno(models.Model):
    nombre_completo = models.CharField(max_length=255)
    matricula = models.CharField(max_length=20)
    usuario = models.CharField(max_length=50, unique=True)
    contrasena = models.CharField(max_length=255)

class Entrega(models.Model):
    codigo = models.TextField()
    puntos_obtenidos = models.IntegerField()
    fecha_hora_entrega = models.DateTimeField(auto_now_add=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
