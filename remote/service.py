# -*- coding: utf-8 -*-

import flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Channel
from tv import TV

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
tv = TV('http://chelsea.local:8090/tv/api/v1.0/')

@app.route('/tv/stop')
def tv_stop():
    tv.stop()
    return flask.redirect(flask.url_for('channels'))

@app.route('/tv/pause')
def tv_pause():
    tv.pause()
    return flask.redirect(flask.url_for('channels'))

@app.route('/tv/play')
def tv_play():
    tv.play()
    return flask.redirect(flask.url_for('channels'))

@app.route('/tv/start/<int:channel_id>')
def tv_start(channel_id):
    channel = db.session.query(Channel).get(channel_id)
    if not channel:
        flask.abort(404)

    tv.start(channel.name, channel.stream)

    return flask.redirect(flask.url_for('channels'))

@app.route('/')
def channels():
    channels = db.session.query(Channel).all()

    return flask.render_template('channels.html', channels=channels)

class Service(object):

    def __init__(self, database=None, host=None, port=None):
        self.database = database
        self.host = host
        self.port = port

    def run(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = self.database

        app.run(host=self.host, port=self.port, debug=True, threaded=True)
