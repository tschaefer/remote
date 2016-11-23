# -*- coding: utf-8 -*-

import csv
from db import Database
from models import Channel
from sqlalchemy.exc import IntegrityError

class Updater(object):

    def __init__(self, csv=None, database=None, verbose=False):
        self.csv = csv
        self.chans = []
        self.db = Database(database=database, verbose=verbose)
        self.db.bind()

    def __del__(self):
        self.db.unbind()

    def read(self):
        with open(self.csv, 'r') as f:
            for chan in csv.DictReader(f):
                self.chans.append(chan)

    def update(self, chan):
        c = Channel()
        c.name = chan['Name']
        c.stream = chan['Stream']
        c.url = chan['Url']
        c.logo = chan['Logo']
        c.feed = chan['Feed']
        self.db.session.add(c)
        try:
            self.db.session.commit()
        except IntegrityError as e:
            self.db.session.rollback()

    def run(self):
        self.read()
        for chan in self.chans:
            self.insert(chan)
