from django.contrib.auth.models import User
from django.db import models

class Comentario(models.Model):
    usuario = models.ForeignKey(User)
    comentario = models.TextField()
