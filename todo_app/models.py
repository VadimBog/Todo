from django.db import models
from django.contrib.auth.models import User




class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']  # sort objects by field complete

    # def get_queryset(self):
    #     return Task.objects.filter(user=self.request.user)
