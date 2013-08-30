from django.test import TestCase

from ..models import Category


class CategoryTestCase(TestCase):
    def setUp(self):
        self.root_category = Category.objects.create(title=u'Programming')
        self.second_category = Category.objects.create(title=u'Python', parent=self.root_category)
        self.third_category = Category.objects.create(title=u'Django', parent=self.second_category)

        self.another_category = Category.objects.create(title=u'Food')

    def test_is_root(self):
        self.assertTrue(self.root_category.is_root)
        self.assertFalse(self.second_category.is_root)
        self.assertFalse(self.third_category.is_root)

    def test_hierarchy(self):
        self.assertEqual(self.root_category.hierarchy(), [
            self.root_category
        ])
        self.assertEqual(self.second_category.hierarchy(), [
            self.root_category, self.second_category]
        )
        self.assertEqual(self.third_category.hierarchy(), [
            self.root_category, self.second_category, self.third_category]
        )

    def test_parents(self):
        self.assertEqual(self.root_category.parents(), [])
        self.assertEqual(self.second_category.parents(), [self.root_category])
        self.assertEqual(self.third_category.parents(), [self.root_category, self.second_category])

    def test_root_parent(self):
        self.assertEqual(self.root_category.root_parent(), self.root_category)
        self.assertEqual(self.second_category.root_parent(), self.root_category)
        self.assertEqual(self.third_category.root_parent(), self.root_category)
        self.assertEqual(self.another_category.root_parent(), self.another_category)

    def test_generate_slug(self):
        self.assertEqual(self.root_category._generate_slug(), u'programming')
        self.assertEqual(self.second_category._generate_slug(), u'programming/python')
        self.assertEqual(self.third_category._generate_slug(), u'programming/python/django')
