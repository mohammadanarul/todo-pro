from django.urls import path
from task.views.class_views import (
    TaskView,
    TaskDetailView,
    TaskUpdateView,
    TaskDeleteView,
    TaskActionView,
)


urlpatterns = [
    path('', TaskView.as_view(), name='home'),
    path('<pk>/detail/', TaskDetailView.as_view(), name='task-detail'),
    path('<pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('<pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('task/<pk>/action', TaskActionView.as_view(), name='task-action')
]