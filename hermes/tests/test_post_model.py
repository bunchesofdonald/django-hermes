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
