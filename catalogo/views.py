
from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto


# Vista basada en función (FBV)
def home(request):
    contexto = {
        "titulo": "Bienvenido al Catálogo Tecnológico",
        "mensaje": "Explora nuestros productos tecnológicos."
    }
    return render(request, "home.html", contexto)


# Vista basada en clase (CBV)
class ProductoListView(ListView):
    model = Producto
    template_name = "catalogo.html"
    context_object_name = "productos"

    def get_queryset(self):
        return Producto.objects.filter(
            stock__gt=0
        ).order_by("precio")
