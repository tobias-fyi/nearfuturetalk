#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'tobias-fyi'
SITENAME = 'Near Future Talk'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

# Theme settings

THEME = "theme/pelican-chunk"

FOOTER_TEXT = "Near Future Talk, FTW!"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('GitHub', 'https://github.com/tobias-fyi/'),
         ('Twitter', 'https://twitter.com/'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/tobias-fyi/'),
          ('Twitter', 'https://twitter.com/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True