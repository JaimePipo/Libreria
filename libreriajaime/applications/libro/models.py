from django.db import models

# from local apps
from applications.autor.models import Autor
from applications.editorial.models import Editorial

# Create your models here.

class Libro(models.Model):
    """Model definition for Libro."""

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    titulo = models.CharField (max_length=50, unique=True)
    portada = models.ImageField(upload_to='portada', blank=True)

    class Meta:
        """Meta definition for Libro."""

        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.titulo
