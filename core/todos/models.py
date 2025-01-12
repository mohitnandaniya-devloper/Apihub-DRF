from django.db import models

class Todo(models.Model):
    tid = models.AutoField(primary_key=True)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    task = models.CharField(max_length=255)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task

