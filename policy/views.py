from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'home.html')
    
def suit(request):
    return render (request, 'suit.html')

def view(request):
    return render (request, 'view.html')