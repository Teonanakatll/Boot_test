from django.contrib import admin

from .models import Chapter, Lesson

class ChapterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'text', 'col']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_editable = ['text']
    list_filter = ['name', 'text']
    # prepopulated_fields = {'slug': ('title',)}

class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'chap']
    list_display_links = ['title']
    search_fields = ['title', 'chap']
    list_editable = ['chap']
    list_filter = ['chap']
    # prepopulated_fields = {'slug': ('title',)}

admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Lesson, LessonAdmin)