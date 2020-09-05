from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request, 'home.html')
    
def suit(request):
    return render (request, 'suit.html')

def view(request):
    return render (request, 'view.html')

def login(request):
    return render (request, 'login.html')

    
def mind(request):
    return render (request, 'mind.html')
    
def mypage(request):
    return render (request, 'mypage.html')
    
def signup(request):
    return render (request, 'signup.html')