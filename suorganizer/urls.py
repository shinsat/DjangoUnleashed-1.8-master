"""suorganizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import (
    index as site_index_view,
    sitemap as sitemap_view)
from django.views.generic import (
    RedirectView, TemplateView)

from blog import urls as blog_urls
from blog.feeds import AtomPostFeed, Rss2PostFeed
from contact import urls as contact_urls
from organizer.urls import (
    startup as startup_urls, tag as tag_urls)
from user import urls as user_urls

from .sitemaps import sitemaps as sitemaps_dict

admin.site.site_header = 'Startup Organizer Admin'
admin.site.site_title = 'Startup Organizer Site Admin'

sitenews = [
    url(r'^atom/$',
        AtomPostFeed(),
        name='blog_atom_feed'),
    url(r'^rss/$',
        Rss2PostFeed(),
        name='blog_rss_feed'),
]

urlpatterns = [
    url(r'^$',
        RedirectView.as_view(
            pattern_name='blog_post_list',
            permanent=False)),
    url(r'^about/$',
        TemplateView.as_view(
            template_name='site/about.html'),
        name='about_site'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include(blog_urls)),
    url(r'^contact/', include(contact_urls)),
    url(r'^sitemap\.xml$',
        site_index_view,
        {'sitemaps': sitemaps_dict},
        name='sitemap'),
    url(r'^sitemap-(?P<section>.+)\.xml$',
        sitemap_view,
        {'sitemaps': sitemaps_dict},
        name='sitemap-sections'),
    url(r'^sitenews/', include(sitenews)),
    url(r'^startup/', include(startup_urls)),
    url(r'^tag/', include(tag_urls)),
    url(r'^user/',
        include(
            user_urls,
            app_name='user',
            namespace='dj-auth')),
]
