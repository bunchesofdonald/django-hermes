"""
Django Hermes | blog.tests.models
Last Update: 05/19/2011
"""

from django.test import TestCase
from hermes.blog.models import *

class EntryModelTestCase(TestCase):
	urls = 'hermes.blog.urls'
	fixtures = ('hermes_blog_test_fixture.json',)

	def test_get_published_entries(self):
		published = Entry.objects.get_published_entries()

		self.assertEqual(len(published), 2)
		self.assertTrue(published[0].id == 1)

	def test_get_for_month(self):
		may_twenty_eleven = Entry.objects.get_for_month(5, 2011)

		self.assertEqual(len(may_twenty_eleven), 2)
		self.assertTrue(may_twenty_eleven[0].id == 1)

	def test_get_for_year(self):
		twenty_eleven = Entry.objects.get_for_year(2011)

		self.assertEqual(len(twenty_eleven), 2)
		self.assertTrue(twenty_eleven[0].id == 1)

	def test_get_absolute_url(self):
		urls = ['/2011/05/19/first-entry','/2011/05/19/second-post']

		for i, url in enumerate(urls):
			entry = Entry.objects.get(id=i+1)
			self.assertEqual(entry.get_absolute_url(), url)
