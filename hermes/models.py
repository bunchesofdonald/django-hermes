from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _
from django.utils.text import Truncator


class TimestampedModel(models.Model):
    created_on = models.DateTimeField(_('created on'), auto_now_add=True)
    modified_on = models.DateTimeField(_('modified on'), auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    title = models.CharField(_('title'), max_length=100)
    parent = models.ForeignKey('self')

    def __unicode__(self):
        return self.title

    def is_root(self):
        return self.parent == None


class PostQuerySet(models.query.QuerySet):
    def recent(self, limit=None):
        queryset = self.all()
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


class Post(TimestampedModel):
    subject = models.CharField(_('subject'), max_length=100)
    slug = models.SlugField(_('slug'), max_length=100)
    summary = models.TextField(_('summary'), blank=True, null=True)
    body = models.TextField(_('body'))
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
