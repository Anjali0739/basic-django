from django.shortcuts import render
from django.http import HttpResponse  # 👈 Step 1: Import built-in response class

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

