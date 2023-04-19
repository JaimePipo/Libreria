from django.db import models

class LibroManager(models.Manager):
    """Este manager le pertenece exclusivamente al modelo 
    Libro de la aplicación libro"""

    def buscar_libro(self, kword=None, autor=None, editorial=None):
        # Comienza con un queryset vacío
        queryset = self.get_queryset()

        # Filtrar por palabra clave (kword) si se proporciona
        if kword:
            queryset = queryset.filter(titulo__icontains=kword)

        # Filtrar por autor si se proporciona
        if autor:
            queryset = queryset.filter(autor=autor)

        # Filtrar por editorial si se proporciona
        if editorial:
            queryset = queryset.filter(editorial=editorial)

        return queryset
