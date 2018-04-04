from django.db import models
from users.models import User

LEVEL_CHOICES = (
    ('u', 'Urgente'),
    ('i', 'Intermedio'),
    ('b', 'Bajo'),
)


class Todo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    user = models.ForeignKey('users.User', related_name='todos', on_delete=models.CASCADE, null=False)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES, default='i')

    class Meta:
        ordering = ('created',)
