from django.db import models

# Create your models here.
class Estudiantes (models.Model):
    cedula_est = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=30, blank=False)
    apelliudo = models.TextField()
    edad = models.TextField()
    direccion = models.TextField()
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
class Docente(models.Model):
    cedula_doc = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=30, blank=False)
    apelliudo = models.TextField()

    def __str__(self):
        return self.nombre
class Calificacion (models.Model):
    cedula_est = models.ForeignKey (Estudiantes, on_delete=models.RESTRICT)
    cedula_doc = models.ForeignKey (Docente, on_delete=models.RESTRICT)
    nota = models.FloatField ()