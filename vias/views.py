from django.shortcuts import render

# Create your views here.
def index(request):
    """
    muestra la pagina princiapl
    """
    return render(request, 'index/index.html')
