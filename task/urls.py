from django.urls import path
from task.views import (
    home_page,
    task_create_view,
    task_update_view,
    task_completed_view, task_view
)


urlpatterns = [
    path('', home_page, name='home'),
    path('task/create/', task_create_view, name='task-create'),
    path('task/<id>/update/', task_update_view, name='task-update'),
    path('task/<pk>/completed/', task_completed_view, name='task-completed'),
    path('task/<pk>/detail/', task_view, name='task-view')
]