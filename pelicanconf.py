#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pierre Guillemot'
SITENAME = 'Side notes of a developer'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Dubai'

DEFAULT_LANG = 'en'

# Theme specific variables
THEME = 'themes/pelican-clean-blog'
COLOR_SCHEME_CSS = 'tomorrow_night.css'
DISABLE_CUSTOM_THEME_JAVASCRIPT = True
FOOTER_INCLUDE = 'custom-footer.html'
IGNORE_FILES = [FOOTER_INCLUDE]
EXTRA_TEMPLATES_PATHS = ['templates']

# Plugins specific variables
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1.0,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Tech-League', 'https://techleague.io/'),
)

# Social widget
SOCIAL = (
    ('Github', 'https://github.com/hnb2'),
    ('Linkedin', 'https://www.linkedin.com/in/pierre-guillemot-32829239/'),
    ('Twitter', 'https://twitter.com/hnb_02')
)

STATIC_PATHS = ['extra/favicon.ico', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

DEFAULT_PAGINATION = 10

TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
