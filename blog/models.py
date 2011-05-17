"""
Django Hermes | blog.models
05/17/2011

Yet another blogging applicaton for django.

Version: 0.1
Author: Chris Pickett
https://github.com/bunchesofdonald/django-hermes/
"""

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

class EntryManager (models.Manager):
	""" Manage a blog's entries. """

	# Archive helpers
	def get_for_year(self, year=datetime.now().year):
		""" Create a queryset of all entries that were posted during the given year. """
		return self.filter(published__year=year).order_by('published')

	def get_for_month(self, month=datetime.now().month, year=datetime.now().year):
		""" Create a queryset of all entries that were posted during the given month/year. """
		return self.get_for_year(year).filter(published__month=month)

class Entry (models.Model):
	""" A blog entry. """
	
	title = models.CharField(max_length=100)

	text = models.TextField()
	html = models.TextField()

	slug = models.SlugField(blank=True)

	author = models.ForeignKey(User)

	# Metadata
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	published = models.DateTimeField()

	objects = EntryManager()

	def get_absolute_url():
		

	def save(self, *args, **kwargs):
		if not self.slug:
			from django.template.defaultfilters import slugify
			self.slug = slugify(self.title)

		from markdown import markdown
		self.html = markdown(self.text)

		super(Entry, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s - %s" % (self.title, self.published)

	class Meta:
		verbose_name_plural = 'Entries'
