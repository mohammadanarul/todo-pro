from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.views import generic
from task.models import Task
from task.forms import Taskform, TaskReportform
from django.urls import reverse_lazy

class TaskView(generic.ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'home.html'

class TaskDetailView(generic.DetailView):
    model = Task
    context_object_name = 'task'
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

class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = Taskform
    template_name = 'task/update.html'
    success_url = '/'


def task_create_view(request):
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META['HTTP_REFERER'])




