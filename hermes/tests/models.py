from django.test import TestCase

from ..models import Category


class CategoryTestCase(TestCase):
    def setUp(self):
        self.root_category = Category.objects.create(title=u'Programming')
        self.second_category = Category.objects.create(title=u'Python', parent=self.root_category)
        self.third_category = Category.objects.create(title=u'Django', parent=self.second_category)

    def test_is_root(self):
        self.assertTrue(self.root_category.is_root)
        self.assertFalse(self.second_category.is_root)
        self.assertFalse(self.third_category.is_root)

    def test_generate_slug(self):
        self.assertEqual(self.root_category._generate_slug(), u'programming')
        self.assertEqual(self.second_category._generate_slug(), u'programming/python')
        self.assertEqual(self.third_category._generate_slug(), u'programming/python/django')
