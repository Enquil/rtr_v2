from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = (
        'author',
        'title',
        'slug',
        'status',
        'created_on',
        'category'
        )
    search_fields = ('title', 'content')
    summernote_fields = ('content')
    actions = ['disable_post']

    def disable_post(self, request, queryset):
        queryset.update(status=2)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
                    'name',
                    'id',
                    'body',
                    'post',
                    'created_on',
                    'approved',
                    'parent_id'
                    )
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['disable_comments']

    def disable_comments(self, request, queryset):
        queryset.update(approved=False)
