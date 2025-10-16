from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello Manikanta!, How are you?.")

def succesPage(request):
    people = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "London"},
    {"name": "Charlie", "age": 28, "city": "Paris"}
]
    return render(request, 'index.html', context={'people': people})

