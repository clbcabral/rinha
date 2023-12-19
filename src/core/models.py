from django.db import models
from django.contrib.postgres.fields import ArrayField

import uuid

# Create your models here.

class Pessoa(models.Model):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4, editable=False)
    apelido = models.CharField(max_length=32, null=False, unique=True)
    nome = models.CharField(max_length=100, null=False)
    nascimento = models.DateField(null=False)
    stack = ArrayField(models.CharField(max_length=32, blank=False), null=True)