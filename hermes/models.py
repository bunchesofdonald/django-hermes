import os

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _
from django.utils.text import Truncator, slugify


class TimestampedModel(models.Model):
    created_on = models.DateTimeField(_('created on'), auto_now_add=True)
    modified_on = models.DateTimeField(_('modified on'), auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    title = models.CharField(_('title'), max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True)
    slug = models.SlugField()

    class Meta:
        verbose_name = u'category'
        verbose_name_plural = u'categories'

    @property
    def full_title(self):
        """
            Returns a '>' separated list of the current category's parents
            title + the current category's title.
        """
        parents = [category.title for category in self.parents()]

        if parents:
            return u"{parents} > {title}".format(
                parents=" > ".join(parents),
                title=self.title,
            )
        else:
            return self.title

    def __unicode__(self):
        return self.full_title

    def _generate_slug(self):
        return "/".join(
            [slugify(parent.title) for parent in self.parents()] + [slugify(self.title)]
        ).lower()

    def parents(self):
        """ Returns a list of all the current category's parents."""
        parents = []

        if self.parent == None:
            return []

        category = self
        while category.parent != None:
            parents.append(category.parent)
            category = category.parent

        return parents

    def is_root(self):
        """ Returns True if this category has no parent. """
        return self.parent == None

    def root_parent(self, category=None):
        """ Gets the topmost parent of the current category. """
        if not category:
            category = self

        if category.is_root():
            return category
        else:
            return self.root_parent(category.parent)


class PostQuerySet(models.query.QuerySet):
    def recent(self, limit=None):
        queryset = self.all()
        if limit:
            queryset = queryset[:limit]

        return queryset

    def random(self, limit=None):
        queryset = self.recent().order_by('?')
        if limit:
            queryset = queryset[:limit]

        return queryset


class PostManager(models.Manager):
    def get_query_set(self):
        return PostQuerySet(Post)

    def __getattr__(self, attr, *args):
        try:
            return getattr(self.__class__, attr, *args)
        except AttributeError:
            return getattr(self.get_query_set(), attr, *args)


def post_hero_upload_to(instance, filename):
    extension = os.path.splitext(filename)[1][1:]

    return "hermes/heroes/{slug}_hero.{extension}".format(
        slug=instance.slug,
        extension=extension
    )


class Post(TimestampedModel):
    hero = models.ImageField(_('hero'), upload_to=post_hero_upload_to)
    subject = models.CharField(_('subject'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100)
    summary = models.TextField(_('summary'), blank=True, null=True)
    body = models.TextField(_('body'))

    category = models.ForeignKey(Category)
    author = models.ForeignKey(User)

    objects = PostManager()

    class Meta:
        ordering = ('-created_on', )

    def __unicode__(self):
        return self.subject

    @models.permalink
    def get_absolute_url(self):
        return ('hermes_post_detail', (), {
            'year': self.created_on.year,
            'month': self.created_on.strftime('%m'),
            'day': self.created_on.strftime('%d'),
            'slug': self.slug,
        })

    @property
    def short(self):
        if self.summary:
            return self.summary
        else:
            return Truncator(self.body).words(30)
