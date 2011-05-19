"""
Django Hermes | blog.models
Last Update: 05/19/2011

EntryManager - Manages a blog's entries
Entry - A blog entry
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.conf import settings

from datetime import datetime

class EntryManager (models.Manager):
	""" Manage a blog's entries. """

	def get_published_entries(self):
		""" Create a queryset of all entries that have a published date of now or in the past. """
		return self.filter(pub_date__lte=datetime.now())

	# Archive helpers
	def get_for_year(self, year=datetime.now().year):
		""" Create a queryset of all entries that were posted during the given year. Defaults to the current year. """
		return self.get_published_entries().filter(pub_date__year=year)

	def get_for_month(self, month=datetime.now().month, year=datetime.now().year):
		""" Create a queryset of all entries that were posted during the given month/year. Defaults to the current month/year.  """
		return self.get_for_year(year).filter(pub_date__month=month)

	def get_for_day(self, day=datetime.now().day, month=datetime.now().month, year=datetime.now().year):
		""" Create a querysey of allentries that were posted doring the given day/month/year. Default to the current day/month/year. """
		return self.get_for_month(month, year).filter(pub_date__day=day)

class Entry (models.Model):
	""" A blog entry. """
	title = models.CharField(max_length=100)

	teaser = models.TextField()
	text = models.TextField()

	teaser_html = models.TextField()
	html = models.TextField()

	slug = models.SlugField(blank=True)
	author = models.ForeignKey(User)

	# Metadata
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	pub_date = models.DateTimeField(blank=True)

	objects = EntryManager()

	def get_absolute_url(self):
		args = {
			'year': self.pub_date.year,
			'month': self.pub_date.strftime('%m'),
			'day': self.pub_date.strftime('%d'),
			'slug': self.slug
		}

		return reverse('hermes_blog_entry_detail', kwargs=args)

	def save(self, *args, **kwargs):
		if not self.slug:
			from django.template.defaultfilters import slugify
			self.slug = slugify(self.title)

		if not self.pub_date:
			self.pub_date = datetime.now()

		self.markup() # Make sure the html version is up-to-date
		
		super(Entry, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s - %s" % (self.title, self.pub_date)

	def markup(self):
		"""
		Marks-up the entry text. 
		Uses markup class defined by settings.HERMES_MARKUP_CLASS.
		Markdown is used by default.
		"""
		try:
			markup_class = settings.__getattr__('HERMES_MARKUP_CLASS')
		except:
			markup_class = 'hermes.blog.markup.languages.Markdown'
		
		markup_module = __import__(".".join(markup_class.split('.')[:-1]), globals(), locals(), [markup_class.split('.')[-1]])
		markup = getattr(markup_module, markup_class.split('.')[-1])
		self.html = markup().markup(self.text)
		self.teaser_html = markup().markup(self.teaser)

	def preview(self):
		pass

	class Meta:
		verbose_name_plural = 'Entries'
