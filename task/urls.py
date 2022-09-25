from django.urls import path
from task.views.class_views import (
    TaskView,
    TaskDetailView,
    TaskUpdateView,
    task_create_view
)


urlpatterns = [
    path('', TaskView.as_view(), name='home'),
    path('<pk>/detail/', TaskDetailView.as_view(), name='task-detail'),
    path('<pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('create/', task_create_view, name='task-create')
]