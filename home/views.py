from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello Manikanta!, How are you?.")

def succesPage(request):
    return render(request, 'index.html')

