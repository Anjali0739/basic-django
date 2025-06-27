from django.shortcuts import render, redirect
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
        return redirect('tasks')  # Prevents re-submitting form on refresh
    
    # Separate queries
    tasks_pending = Task.objects.filter(completed=False).order_by('-created')
    tasks_done = Task.objects.filter(completed=True).order_by('-created')
    return render(request, 'task.html', {
        'tasks_pending': tasks_pending,
        'tasks_done': tasks_done
    })


def mark_done(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('tasks')



def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('tasks')
