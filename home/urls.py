from django.urls import path
from . import views  # 👈 Import the views file from same folder

urlpatterns = [
    path('', views.home_view, name='home'),  # 👈 Home page route
    path('about/', views.about_view, name='about'),  # 👈 About page route
    path('contact/', views.contact_view, name='contact'),  # 👈 New Contact route
    path('task/', views.task_view, name='task'),  # 👈 New Task route
    path('task/done/<int:task_id>/', views.mark_done, name='mark_done'),
    path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
