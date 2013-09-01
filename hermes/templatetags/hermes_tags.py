from django import template

from hermes.models import Post

register = template.Library()


@register.inclusion_tag('hermes/random_post_list.html')
def random_posts(path, limit=3):
    return {
        'posts': Post.objects.random(limit=limit),
    }
