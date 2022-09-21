from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import Task
from .forms import Taskform, TaskReportform

def home_page(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

def task_view(request, pk):
    form = TaskReportform()
    task = Task.objects.get(pk=pk)
    context = {
        'task': task,
        'form': form,
    }
    return render(request, 'task/detail.html', context)

def task_completed_view(request, pk):
    task = Task.objects.get(pk=pk)
    if task.is_completed:
        task.is_completed = False
        task.save()
    else:
        task.is_completed= True
        task.save()
    return redirect(request.META['HTTP_REFERER'])


def task_create_view(request):
    form = Taskform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'task/create.html', {'form': form})

def task_update_view(request, id):
    task = Task.objects.get(pk=id)
    form = Taskform(request.POST or None, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'task/update.html', {'form': form})