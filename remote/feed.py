# -*- coding: utf-8 -*-

import feedparser
import re

class Feed(object):

    def __init__(self, rss, channel):
        self.rss = rss
        self.channel = channel
        self.entry = None

    def _entry(self):
        feed = feedparser.parse(self.rss)
        for entry in feed['entries']:
            if entry['title'].startswith(self.channel):
                self.entry = entry

    def _elements(self):
        _, self.title = self.entry['title'].split(': ', 1)
        raw = re.search('[0-9]{1,2}:[0-9]{1,2} - [0-9]{1,2}:[0-9]{1,2}', self.entry['summary'])
        self.date = raw.group(0)
        raw = re.search('src=.+\.jpg', self.entry['summary'])
        self.img = None
        if raw:
            self.img = raw.group(0).split('"')[1]
        self.link = self.entry['link']

    def parse(self):
        self._entry()
        self._elements()
