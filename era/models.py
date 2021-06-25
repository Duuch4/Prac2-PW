from django.db import models

# Create your models here.
from django.urls import reverse


class Facultad(models.Model):
    id_Facultad = models.AutoField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('era:facultad_details', kwargs={'pk': self.pk})

class Carrera(models.Model):
    id_carrera = models.AutoField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=45)
    abreviado = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    Facultad_idFacultad = models.ForeignKey(Facultad, on_delete= models.CASCADE,default="1")

    def get_absolute_url(self):

        return reverse('era:career_details', kwargs={
            'pk': self.Facultad_idFacultad.id_Facultad,
            'pkr': self.pk,
        })

    def get_facultad(self):
        return Facultad.objects.get(pk=self.Facultad_idFacultad.pk)


class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=45)
    lastname = models.CharField(max_length=55)
    semestre = models.IntegerField()
    telefono = models.CharField(max_length=9)
    correo = models.CharField(max_length=60)
    clave = models.CharField(max_length=35)
    fecha_nac= models.DateTimeField()
    Genero = models.CharField(max_length=20)
    Carrera_idCarrera = models.ForeignKey(Carrera, on_delete = models.CASCADE ,default="1")
    Intercambio_idintercambio = models.ForeignKey(Intercambio, on_delete = models.CASCADE ,default="1")


