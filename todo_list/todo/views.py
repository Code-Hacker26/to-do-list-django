# todo/views.py
from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)  
    task.delete()  
    return redirect('task_list')  
