from django.contrib import admin

from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("subject", )}


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
