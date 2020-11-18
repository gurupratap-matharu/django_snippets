from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Language(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Snippet(models.Model):
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
        return reverse("snippet_detail", args=[self.language.slug, self.name])
