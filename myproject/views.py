from django.shortcuts import render


def index(request):
    """Renderiza la página de inicio del proyecto."""
    return render(request, "index.html")