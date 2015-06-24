 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from application import db
import datetime





class newsLetterEmail(db.Model):
	
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(128), nullable=False)


	def __init__(self, email):
		self.email = email

	def __repr__(self):
		return '<User %r>' % self.id




class userContact(db.Model):
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(256), nullable=False)
	email = db.Column(db.String(128), nullable=False)
	phonenumber = db.Column(db.String(54), nullable=False)


	def __init__(self, name, email, phonenumber):
		self.name = name
		self.email = email
		self.phonenumber = phonenumber

	def __repr__(self):
		return '<userContact %r>' % self.id

