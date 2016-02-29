#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jeffrey W. Miller'
SITENAME = u"Miller's notebook"
SITEURL = ''

#### BEGIN CUSTOMIZATIONS #####
# Theme settings
THEME = 'pelican-alchemy/alchemy'
SITE_SUBTEXT = 'Notes on my research in statistics and its applications'
HOME_ON_MENU = True
PAGES_ON_MENU = True
ARCHIVES_ON_MENU = True
LICENSE_NAME = 'Creative Commons Attribution 4.0 International License'
LICENSE_URL = 'http://creativecommons.org/licenses/by/4.0/'
GITHUB_ADDRESS = 'http://github.com/jwmi'
META_DESCRIPTION = SITENAME

#### END CUSTOMIZATIONS #####

########
PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 50

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
