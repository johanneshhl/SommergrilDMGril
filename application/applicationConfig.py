import os
import datetime


PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=365)
SESSION_COOKIE_PATH = '/'

APPLICATION_NAME = u'Sommergril'
APPLICATION_OWNER = u'Johannes Hvilsom Larsen'
APPLICATION_VERSION = u'0.1'


if 'DYNO' not in os.environ:
	APPLICATION_MODE = u'localhost'
	DEBUG = True
	PREFERRED_URL_SCHEME = 'http'
	SESSION_COOKIE_DOMAIN = '0.0.0.0'
else:
	APPLICATION_MODE = u'Heroku'
	SERVER_NAME = 'damp-wave-4063.herokuapp.com'
	SESSION_COOKIE_DOMAIN = '.damp-wave-4063.herokuapp.com'
	SESSION_COOKIE_SECURE = True
	SESSION_COOKIE_NAME = 'herokuSession'
	PREFERRED_URL_SCHEME = 'http'
	DEBUG = True


UPLOAD_FOLDER = 'static/assets'


SECRET_KEY = u'\x89\x15\xbe\x8c\x93\xf0k\xee\x91\xe0\xae\xba\xb3?\xdc\xa9\xe1ns8\xceVe]'

#set up localhost usage
if not os.environ.has_key('DATABASE_URL'):
	os.environ['DATABASE_URL'] = 'postgres://localhost:5432'
else:
	os.environ['DATABASE_URL'] = 'postgres://tzlbdqonwabfwn:gr-ukyEwHidOs6CGWOudrwHhOa@ec2-54-217-202-108.eu-west-1.compute.amazonaws.com:5432/da1cn5233q44ih'
	
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


del datetime
del os