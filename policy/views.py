from django.shortcuts import render, redirect, get_object_or_404
from .models import Policies
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render (request, 'home.html')
    
def suit(request): 
    policies = Policies.objects.all() 
    return render(request, 'suit.html', {'policies' : policies})  
def view(request):
     policies = Policies.objects.all() 
     return render (request, 'view.html', {'policies' : policies})

def suit(request): 
    policies = Policies.objects.all() 
    return render(request, 'suit.html', {'policies' : policies})
    

def login(request):
    return render (request, 'login.html')    

def mind(request):
    return render (request, 'mind.html')
    
def mypage(request):
    return render (request, 'mypage.html')
    
def signup(request):
    regi_form = UserCreationForm()
    if request.method == "POST":
        filled_form = UserCreationForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('login')
    return render (request, 'signup.html', {'regi_form':regi_form})


def blog_gugic(request):
    return render (request, 'blog_gugic.html')

def blog_education(request):
    return render (request, 'blog_education.html')


def filteraside(request):
    return render (request, 'filteraside.html')
    
def search(request):
    policies = Policies.objects.all()

    q = request.POST.get('q') 

    if q:
        policies = policies.filter(name__icontains=q)
        return render(request, 'search.html', {'policies' : policies, 'q' : q})
    
    else:
        return render(request, 'search.html')

def detail(request, policy_id): # views.py의 pk 변수명과 urls.py의 변수명은 같아야 함
    policy = get_object_or_404(Policies, pk = policy_id)
    return render(request, 'detail.html', {'policy' : policy})

# def category(request) :

#     categories = Policies.objects.all() 
#     category_text = request.POST.get()

#     if category_text:
#         categories = categories.objects.filter( category__icontains = category_text )
#         return render(request, 'category.html', {'categories' : categories, 'category_text':category_text})

