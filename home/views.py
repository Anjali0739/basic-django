from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse  # 👈 Step 1: Import built-in response class
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

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


@login_required
def task_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title, user=request.user)  # 👈 Save task for current user
        return redirect('task')  # Prevents re-submitting form on refresh
    
    # Separate queries
    tasks_pending = Task.objects.filter(user=request.user, completed=False).order_by('-created')
    tasks_done = Task.objects.filter(user=request.user, completed=True).order_by('-created')
    return render(request, 'task.html', {
        'tasks_pending': tasks_pending,
        'tasks_done': tasks_done
    })

@login_required
def mark_done(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = True
    task.save()
    return redirect('task')


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('task')



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task')
        else:
            messages.error(request, form.errors)
            print(form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)  # ✅ ends the session
    return redirect('login')  # ✅ redirects to login page