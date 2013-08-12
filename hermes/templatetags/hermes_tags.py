from django import template

from hermes.models import Post

register = template.Library()


@register.inclusion_tag('hermes/post_list_include.html')
def random_posts(path, limit=3):
    return {
        'posts': Post.objects.random(limit=limit),
    }
