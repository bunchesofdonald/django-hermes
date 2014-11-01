import feedparser

from . import HermesTestCase
from .. import models


class LatestPostFeedTestCase(HermesTestCase):
    def url(self):
        return super(LatestPostFeedTestCase, self).url('hermes_post_feed')

    def test_feed_contains_posts(self):
        response = self.get(self.url())
        data = feedparser.parse(response.content)

        post_urls = [post['id'] for post in data['entries']]
        expected = [
            "http://testserver{url}".format(url=post.get_absolute_url())
            for post in models.Post.objects.all()
        ]

        self.assertEqual(expected, post_urls)
