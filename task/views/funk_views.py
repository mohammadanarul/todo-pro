from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from task.models import Task
from task.forms import Taskform, TaskReportform

def home_page(request):
    tasks = Task.objects.all()
    # form = Taskform(request.POST or None)
    # if request.method == 'POST':
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')
    context = {
        'tasks': tasks,
        # 'form': form,
    }
    return render(request, 'home.html', context)

def task_view(request, pk):
    form = TaskReportform(request.POST or None)
    try:
        task = Task.objects.get(pk=pk)
    except task.DoesNotExist:
        return redirect('home')
    task_report = task.task_reports.all()
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.task = task
            obj.save()
            return redirect(request.META['HTTP_REFERER'])
    context = {
        'task': task,
        'form': form,
        'task_report': task_report,
    }
    return render(request, 'task/detail.html', context)

def task_completed_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.is_completed:
        task.is_completed = False
    else:
        task.is_completed= True
    task.save()
    return redirect(request.META['HTTP_REFERER'])


def task_create_view(request):
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META['HTTP_REFERER'])

def task_update_view(request, id):
    task = Task.objects.get(pk=id)
    form = Taskform(request.POST or None, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'task/update.html', {'form': form})