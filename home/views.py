from django.shortcuts import render
from django.http import HttpResponse  # 👈 Step 1: Import built-in response class
from .models import Task

# Create your views here.


# def home_view(request):              # 👈 Step 2: Define a function for homepage
#     return HttpResponse("Hello, this is the Home Page!")  # 👈 Step 3: Return plain text as HTML


def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        return render(request, 'contact.html', {
            'name': name,
            'message': message
        })
    return render(request, 'contact.html')



def task_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
    tasks = Task.objects.all().order_by('-created')
    return render(request, 'task.html', {'tasks': tasks})

