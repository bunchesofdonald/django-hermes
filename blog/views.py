"""
EntryDetailView - Displays entry's details.
EntryListView - Displays the most recent entries.
EntryArchiveListView - Displays a list of entries based on given date.

Django Hermes | blog.views
05/18/2011

Author: Chris Pickett
https://github.com/bunchesofdonald/django-hermes/
"""

from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator
from django.conf import settings

from hermes.blog.models import Entry

class EntryDetailView(DetailView):
	"""
	Displays an entry's details.

	get_object: Uses get_object_or_404 to do a lookup on Entry, using the given date and slug.
	"""

	template_name = 'hermes-blog/entry_details.html'
	context_object_name = 'entry'

	def get_object(self):
		filter = {
			'published__year': self.kwargs['year'],
			'published__month': self.kwargs['month'],
			'published__day': self.kwargs['day'],
			'slug': self.kwargs['slug']
		}

		return get_object_or_404(Entry, **filter)

class EntryListView(ListView):
	""" Displays the most recent entries """

	try:
		entries_per_page = settings.__getattr__('HERMES_ENTRIES_PER_PAGE')
	except AttributeError:
		entries_per_page = 10

	template_name = 'hermes-blog/entry_list.html'
	context_object_name = 'entries'
	paginate_by = entries_per_page

	def get_queryset(self):
		return Entry.objects.all().order_by('-published')

class EntryArchiveListView(EntryListView):
	""" Displays all entries for the given date. """

	def get_queryset(self):
		if 'day' in self.kwargs:
			return Entry.objects.get_for_day(self.kwargs['day'], self.kwargs['month'], self.kwargs['year'])
		if 'month' in self.kwargs:
			return Entry.objects.get_for_month(self.kwargs['month'], self.kwargs['year'])
		else:
			return Entry.objects.get_for_year(self.kwargs['year'])
