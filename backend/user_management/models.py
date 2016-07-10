from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    message = models.TextField(null=False, blank=False)

    class Meta:
        ordering = ('created',)
