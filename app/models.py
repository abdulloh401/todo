from django.db import models


class Tasks(models.Model):
    task = models.CharField(max_length=500)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
