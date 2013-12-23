from django import test
from django.core import urlresolvers


from .. import models


class HermesTestCase(test.TestCase):
    fixtures = ('hermes', )

    def setUp(self):
        # Instantiate Categories
        self.root_category = models.Category.objects.get(slug='programming')
        self.second_category = models.Category.objects.get(slug='programming/python')
        self.third_category = models.Category.objects.get(slug='programming/python/django')
        self.another_category = models.Category.objects.get(slug=u'food')

        # Instatiate Posts
        self.post1 = models.Post.objects.get(id=1)
        self.post2 = models.Post.objects.get(id=2)
        self.post3 = models.Post.objects.get(id=3)
        self.post4 = models.Post.objects.get(id=4)

        self.client = test.Client()

    def url(self, url_name, *args, **kwargs):
        return urlresolvers.reverse(url_name, args=args, kwargs=kwargs)

    def get(self, url):
        return self.client.get(url)
