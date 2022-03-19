from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from blog.models import Blog, Contact
# Create your views here.
def home(request):
    return render(request, 'index.html')

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs' : blogs}
    return render(request, 'bloghome.html', context)

def search(request):
     return render(request, 'search.html')

def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog' : blog}

    return render(request, 'blogpost.html', context)

def contact(request):
   
    if request.method=="POST":
        
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(name, email, phone, desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("The data has been written to the db")
    return render(request, 'contact.html')
   