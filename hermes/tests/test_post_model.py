from . import HermesTestCase
from .. import models, settings


class PostTestCase(HermesTestCase):
    def test_short(self):
        """A Post should return the truncated body if there is no summary"""
        expected = (
            u"I've got to find a way to escape the horrible ravages of youth. "
            u"Suddenly, I'm going to the bathroom like clockwork, every three "
            u"hours. And those jerks at Social Security..."
        )
        self.assertEqual(expected, self.post1.short)

    def test_short_with_summary(self):
        """A Post should return the summary if there is one"""
        expected = u"This is a summary"
        self.post1.summary = expected
        self.post1.save()

        self.assertEqual(expected, self.post1.short)

    def test_rendered(self):
        """A Post should be able to render its body into HTML"""
        self.post4.body = "##Markdown FTW!"
        self.post4.save()

        expected = "<h2>Markdown FTW!</h2>"

        self.assertEqual(expected, self.post4.rendered)

    def test_rendereded_no_renderer(self):
        """A Post should return its body if no renderer is defined"""
        renderer = settings.MARKUP_RENDERER
        settings.MARKUP_RENDERER = None

        expected = self.post1.body
        self.assertEqual(expected, self.post1.rendered)

        settings.MARKUP_RENDERER = renderer

    def test_hero_upload_to(self):
        """The Post Hero Upload To method should know the path to save the Hero image"""
        expected = "hermes/heroes/leela-her-own_hero.jpg"
        self.assertEqual(expected, models.post_hero_upload_to(self.post1, 'test.jpg'))

        expected = "hermes/heroes/raging-bender_hero.jpg"
        self.assertEqual(expected, models.post_hero_upload_to(self.post3, 'test.jpg'))

    def test_unicode(self):
        """The Post should have a unicode representation"""
        expected = u"A Tale of Two Santas"
        self.assertEqual(expected, self.post2.__unicode__())

        expected = u"The Series Has Landed"
        self.assertEqual(expected, self.post4.__unicode__())

    def test_get_absolute_url(self):
        """The Post should know its absolute URL"""
        expected = "/blog/2010/06/10/leela-her-own/"
        self.assertEqual(expected, self.post1.get_absolute_url())

        expected = "/blog/2013/09/10/series-has-landed/"
        self.assertEqual(expected, self.post4.get_absolute_url())


class PostQuerySetTestCase(HermesTestCase):
    def test_reverse_creation_order(self):
        """The Post QuerySet should return Posts in reverse creation order"""
        expected = [self.post4, self.post3, self.post2, self.post1, ]
        self.assertEqual(expected, list(models.Post.objects.all()))

    def test_in_category(self):
        """The Post QuerySet should return Posts in a specific Category"""
        expected = [self.post3, self.post2, self.post1, ]
        self.assertEqual(expected, list(models.Post.objects.in_category('programming')))

    def test_in_category_children(self):
        """The Post QuerySet should return Posts in a specific Category and its Children"""
        self.post1.category = self.third_category
        self.post1.save()

        self.post2.category = self.second_category
        self.post2.save()

        expected = [self.post2, self.post1, ]
        self.assertEqual(expected, list(models.Post.objects.in_category('programming/python')))

    def test_recent(self):
        """The PostQuerySet recent method should return the most recent Posts up to 'limit'"""
        expected = [self.post4, self.post3, ]
        self.assertEqual(expected, list(models.Post.objects.recent(limit=2)))

    def test_recent_no_limit(self):
        """The PostQuerySet recent method should return all the Posts if no limit is set"""
        expected = [self.post4, self.post3, self.post2, self.post1, ]
        self.assertEqual(expected, list(models.Post.objects.recent(limit=None)))

    def test_random(self):
        """The PostQuerySet random method should return a random set of Posts"""
        unexpected = models.Post.objects.random(limit=3)
        self.assertNotEqual(unexpected, models.Post.objects.random(limit=3))
        self.assertTrue(
            all(
                isinstance(post, models.Post)
                for post in models.Post.objects.random(limit=3)
            )
        )

    def test_created_on_year(self):
        """The PostQuerySet should know which Posts were created in which year"""
        expected = [self.post1, ]
        self.assertEqual(expected, list(models.Post.objects.created_on(year=2010)))

        expected = [self.post2, ]
        self.assertEqual(expected, list(models.Post.objects.created_on(year=2011)))

    def test_created_on_month_year(self):
        """The PostQuerySet should know which Posts were created in which month/year"""
        expected = [self.post3, ]
        self.assertEqual(expected, list(models.Post.objects.created_on(year=2012, month=8)))

        expected = [self.post4, ]
        self.assertEqual(expected, list(models.Post.objects.created_on(year=2013, month=9)))

    def test_created_on_month_year_day(self):
        """The PostQuerySet should know which Posts were created in which day/month/year"""
        expected = [self.post1, ]
        self.assertEqual(
            expected, list(models.Post.objects.created_on(year=2010, month=6, day=10)))

        expected = [self.post3, ]
        self.assertEqual(
            expected, list(models.Post.objects.created_on(year=2012, month=8, day=10)))
