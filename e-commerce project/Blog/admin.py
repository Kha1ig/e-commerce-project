from django.contrib import admin
from Blog.models import Author, Blog, Category, Comment
# Register your models here.

@admin.register(Blog)

class Blog(admin.ModelAdmin):
    list_display = ('title', 'author', 'category')
    list_display_links = list_display
    search_fields = ('title', 'author', )
    search_help_text = ('find by title or author')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(status = 'approve') 


#admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Comment)