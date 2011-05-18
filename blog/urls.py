from django.conf.urls.defaults import patterns, include, url

from hermes.blog.views import *

urlpatterns = patterns('',
    url(r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>.+)', EntryDetailView.as_view(), name='hermes_blog_entry_detail'),

		# Archive Patterns
		url(r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})', EntryArchiveListView.as_view(), name='hermes_blog_entry_archive_day'),
		url(r'(?P<year>\d{4})/(?P<month>\d{2})', EntryArchiveListView.as_view(), name='hermes_blog_entry_archive_month'),
		url(r'(?P<year>\d{4})', EntryArchiveListView.as_view(), name='hermes_blog_entry_archive_year'),

		url(r'', EntryListView.as_view(), name='hermes_blog_entry_list'),
)
