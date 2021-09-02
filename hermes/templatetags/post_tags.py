from django import template
register = template.Library()

from hermes.models import Post

def posts_for_tag(tag):
    posts = Post.objects.for_tag(tag)[:3]
    return {'posts': posts}


register.inclusion_tag('hermes/posts_for_tag.html')(posts_for_tag)
