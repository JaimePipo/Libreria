from django.shortcuts import render

from django.views.generic import (
    ListView
)

from applications.libro.models import Libro

# Create your views here.

class HomePageView(ListView):
    template_name = 'home/index.html'
    paginate_by = 6
 
    def get_queryset(self):
        # Obtiene los parámetros de la URL
        kword = self.request.GET.get('kword', '')
        autor = self.request.GET.get('autor', '')
        editorial = self.request.GET.get('editorial', '')

        # Filtra los libros utilizando el manager personalizado
        queryset = Libro.objects.buscar_libro(kword, autor, editorial)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['libros'] = self.get_queryset()
        
        return context