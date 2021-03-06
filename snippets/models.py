from __future__ import unicode_literals

import uuid

from django.contrib.auth import get_user_model
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
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='snippets')
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
        return reverse('snippet_detail', args=[self.language.slug, self.id])

    def get_update_url(self):
        return reverse('snippet_update', args=[self.id])

    def get_delete_url(self):
        return reverse('snippet_delete', args=[self.id])

    def can_update(self, user):
        return user.is_superuser or self.user == user

    def can_delete(self, user):
        return user.is_superuser or self.user == user
