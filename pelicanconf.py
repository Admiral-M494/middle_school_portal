#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Madhav Karnati'
SITENAME = 'Middle School Portal'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Facebook', 'https://www.facebook.com/williamsmiddleibptsa/'),
         ('Twitter', 'https://twitter.com/williamsibmyp?lang=en'),
        #  ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
        #  ('You can modify those links in your config file', '#'),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 15

NEWEST_FIRST_ARCHIVES = True
ARTICLE_ORDER_BY = 'reversed-date'

PLUGINS = ['pelican-plotly']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True