from django.db import models

# Create your models here.

class Autor(models.Model):
    """Model definition for Autor"""

    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        """Meta definition for Autor."""

        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nombre