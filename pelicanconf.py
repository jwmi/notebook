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
#PROFILE_IMAGE = 'images/coffee-table-small.jpg'

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math','disqus_static']

# Disqus (comments)
DISQUS_SITENAME = u'millersnotebook'
DISQUS_SECRET_KEY = u'4N6PXCPDSpJT9A0EhpUChp5BUCOoT5sIBUW1hYKc08iPQG7oPuyY6TL71gjnofQ2'
DISQUS_PUBLIC_KEY = u'VgW0p6k1CzIL7WT1TKJPvgBYu46ZKylVRo5cMuctZ9VtvHgH2NL7OmnNphikiKq7'

# Paths
STATIC_PATHS = [
    'images', 
    'extra/favicon.ico'
]
EXTRA_FAVICON = True
    #'extra/robots.txt', 
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
    #'extra/robots.txt': {'path': 'robots.txt'},

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
#RELATIVE_URLS = True
