from . import HermesTestCase
from .. import models


class PostListViewTestCase(HermesTestCase):
    def url(self):
        return super(PostListViewTestCase, self).url('hermes_post_list')

    def test_context_contains_posts(self):
        """The PostListView Context should contain a QuerySet of all Posts"""
        response = self.get(self.url())
        expected = list(models.Post.objects.all())
        self.assertEqual(expected, list(response.context['posts']))


class CategoryPostListViewTestCase(HermesTestCase):
    def url(self, category):
        return category.get_absolute_url()

    def test_context_contains_posts(self):
        """The CategoryPostListView Context should contain a QuerySet of all
        Posts in the given Category
        """
        response = self.get(self.url(self.root_category))
        expected = list(models.Post.objects.filter(category=self.root_category))
        self.assertEqual(expected, list(response.context['posts']))


class ArchivePostListViewTestCase(HermesTestCase):
    def url(self, year=None, month=None, day=None):
        if year and month and day:
            url_name = 'hermes_archive_year_month_day'
            kwargs = {'year': year, 'month': month, 'day': day, }
        elif year and month:
            url_name = 'hermes_archive_year_month'
            kwargs = {'year': year, 'month': month, }
        else:
            url_name = 'hermes_archive_year'
            kwargs = {'year': year, }

        return super(ArchivePostListViewTestCase, self).url(url_name, **kwargs)

    def test_context_contains_posts_by_month_year_day(self):
        """The ArchivePostListView Context should contain a QuerySet of all
        Posts on the given month/day/year
        """
        response = self.get(self.url(year=2010, month=6, day=10))
        expected = list(models.Post.objects.created_on(year=2010, month=6, day=10))
        self.assertEqual(expected, list(response.context['posts']))

    def test_context_contains_posts_by_month_year(self):
        """The ArchivePostListView Context should contain a QuerySet of all
        Posts on the given month/day
        """
        response = self.get(self.url(year=2011, month=7))
        expected = list(models.Post.objects.created_on(year=2011, month=7))
        self.assertEqual(expected, list(response.context['posts']))

    def test_context_contains_posts_by_year(self):
        """The ArchivePostListView Context should contain a QuerySet of all
        Posts in the given year
        """
        response = self.get(self.url(year=2012))
        expected = list(models.Post.objects.created_on(year=2012))
        self.assertEqual(expected, list(response.context['posts']))


class PostDetailViewTestCase(HermesTestCase):
    def url(self, post):
        return post.get_absolute_url()

    def test_context_contains_post(self):
        response = self.get(self.url(self.post1))
        expected = self.post1
        self.assertEqual(expected, response.context['post'])
