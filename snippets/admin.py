from django.contrib import admin

from .models import Language, Snippet


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'public', 'language', 'user', 'created',)
    list_filter = ('public', 'created', 'updated',)
    list_editable = ('public',)
    search_fields = ('name', 'description', 'snippet',)
    raw_id_fields = ('user',)
    date_hierarchy = 'created'
    ordering = ('public', 'created')


admin.site.register(Language, LanguageAdmin)
admin.site.register(Snippet, SnippetAdmin)
