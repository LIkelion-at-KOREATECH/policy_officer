from django.shortcuts import render, get_object_or_404
from .models import Policies

# Create your views here.
def home(request):
    return render (request, 'home.html')
    
def suit(request): 
    policies = Policies.objects.all() 
    return render(request, 'suit.html', {'policies' : policies})  
def view(request):
     return render (request, 'view.html')

def login(request):
    return render (request, 'login.html')

def customize(request):
    return render (request, 'customize.html')    

def mind(request):
    return render (request, 'mind.html')
    
def mypage(request):
    return render (request, 'mypage.html')
    
def signup(request):
    return render (request, 'signup.html')

def edu(request):
    return render (request, 'edu.html')
def blog_covid(request):
    return render (request, 'blog_covid.html')
def blog_gugic(request):
    return render (request, 'blog_gugic.html')
def blog_education(request):
    return render (request, 'blog_education.html')
def blog_tom(request):
    return render (request, 'blog_tom.html')
def blog_k(request):
    return render (request, 'blog_k.html')
def filteraside(request):
    return render (request, 'filteraside.html')
def search(request):
    policies = Policies.objects.all().order_by('-id')




    q = request.POST.get('q', "") 

    if q:
        policies = policies.filter(name__icontains=q)
        return render(request, 'search.html', {'policies' : policies, 'q' : q})
    
    else:
        return render(request, 'search.html')

def detail(request, policy_id): # views.py의 pk 변수명과 urls.py의 변수명은 같아야 함
    policy = get_object_or_404(Policies, pk = policy_id)
    return render(request, 'detail.html', {'policy' : policy})



