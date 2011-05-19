from django.contrib import admin

from hermes.blog.models import Entry

class EntryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	exclude = ('teaser_html','html','author')

	def save_model(self, request, obj, form, change):
		""" If obj is a new entry, sets the author to the current user. """
		if not change:
			obj.author = request.user
		obj.save()

admin.site.register(Entry, EntryAdmin)
