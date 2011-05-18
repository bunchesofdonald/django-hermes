"""
Managers:
	EntryManager - Manages a blog's entries

Models:
	Entry - A blog entry

Django Hermes | blog.models
05/18/2011

Author: Chris Pickett
https://github.com/bunchesofdonald/django-hermes/
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from datetime import datetime

class EntryManager (models.Manager):
	""" Manage a blog's entries. """

	# Archive helpers
	def get_for_year(self, year=datetime.now().year):
		""" Create a queryset of all entries that were posted during the given year. Defaults to the current year. """
		return self.filter(published__year=year).order_by('published')

	def get_for_month(self, month=datetime.now().month, year=datetime.now().year):
		""" Create a queryset of all entries that were posted during the given month/year. Defaults to the current month/year.  """
		return self.get_for_year(year).filter(published__month=month)

	def get_for_day(self, day=datetime.now().day, month=datetime.now().month, year=datetime.now().year):
		""" Create a querysey of allentries that were posted doring the given day/month/year. Default to the current day/month/year. """
		return self.get_for_month(month, year).filter(published__day=day)

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

	def get_absolute_url(self):
		args = {
			'year': self.published.year,
			'month': self.published.strftime('%m'),
			'day': self.published.strftime('%d'),
			'slug': self.slug
		}

		return reverse('hermes_blog_entry_detail', kwargs=args)

	def save(self, *args, **kwargs):
		if not self.slug:
			from django.template.defaultfilters import slugify
			self.slug = slugify(self.title)

		self.markup() # Make sure the html version is up-to-date
		
		super(Entry, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s - %s" % (self.title, self.published)

	def markup(self):
		""" 
		Marks-up the entry text. Uses markdown by default.

		TODO: Make this more flexible so that it can handle multiple mark-up languages.
		"""

		from markdown import markdown
		self.html = markdown(self.text)
	
	def preview(self):
		pass

	class Meta:
		verbose_name_plural = 'Entries'
