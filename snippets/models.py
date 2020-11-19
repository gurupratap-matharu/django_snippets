from __future__ import unicode_literals

import uuid

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Language(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name


class Snippet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='snippets')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='snippets')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    snippet = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"Snippet {self.name} in {self.language} by {self.user} "

    def get_absolute_url(self):
        return reverse("snippet", args=[self.id])
