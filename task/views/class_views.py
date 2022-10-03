from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView, 
    DeleteView,
    DetailView,
    UpdateView,
    ListView,
    View
)
from task.models import Task
from task.forms import Taskform, TaskReportform
from django.urls import reverse_lazy

class TaskView(CreateView, ListView):
    model = Task
    form_class = Taskform
    context_object_name = 'tasks' # object_list
    template_name = 'home.html'
    success_url = reverse_lazy('home') # http -> 302


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task' # object
    template_name = 'task/detail.html'

    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        context['form'] = TaskReportform
        return context
    
    def post(self, request, *args, **kwargs):
        form = TaskReportform(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.task = self.get_object()
            obj.save()
            return redirect(request.META['HTTP_REFERER'])


class TaskUpdateView(UpdateView):
    model = Task
    form_class = Taskform
    template_name = 'task/update.html'
    success_url = '/'

class TaskActionView(View):
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        if task.is_completed == True:
            task.is_completed = False
        else:
            task.is_completed = True
        task.save()
        return redirect('/')



class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task/delete.html'
    success_url = '/'






