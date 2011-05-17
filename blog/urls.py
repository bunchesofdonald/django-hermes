from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>\w+)', 'hermes.blog.views.detail', name='hermes_blog_entry_detail'),
)

