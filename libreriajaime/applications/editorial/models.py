from django.db import models

# Create your models here.

class Editorial(models.Model):
    """Model definition for Editorial."""

    nombre_editorial = models.CharField(max_length=50, unique=True)

    class Meta:
        """Meta definition for Editorial."""

        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'

    def __str__(self):
        return self.nombre_editorial