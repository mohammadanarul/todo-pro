from django import forms
from django.forms import ModelForm
from django.forms import TextInput
from .models import Task, TaskReport


class Taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
                'placeholder': 'task title'})
        }


class TaskReportform(forms.ModelForm):
    class Meta:
        model = TaskReport
        fields = ('description',)
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out',
                'placeholder': 'task report'})
        }