from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)


# Create your models here.
class Task(BaseModel):
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)


class TaskReport(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True, related_name='task_reports')
    description = models.TextField()

'''
OneToMany == Foreignkey
'''