 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from application import app, request, redirect, escape, session, url_for, db, render_template, g, flash

@app.route('/')
def index():


	'''
		Hvis brugeren er logget ind, hvis forside
		Ellers hvis "spalshpage", hvor man kan oprette bruger og logge ind

	'''

	return render_template('forside.html')


@app.route('/opskrifter')
def opskrifter():


	'''
		Hvis brugeren er logget ind, hvis forside
		Ellers hvis "spalshpage", hvor man kan oprette bruger og logge ind

	'''

	return render_template('opskrifter.html')



@app.route('/gril')
def gril():


	'''
		Hvis brugeren er logget ind, hvis forside
		Ellers hvis "spalshpage", hvor man kan oprette bruger og logge ind

	'''

	return render_template('gril.html')


@app.route('/produkter')
def produkter():


	'''
		Hvis brugeren er logget ind, hvis forside
		Ellers hvis "spalshpage", hvor man kan oprette bruger og logge ind

	'''

	return render_template('produkter.html')




@app.route('/bestil')
def bestil():


	'''
		Hvis brugeren er logget ind, hvis forside
		Ellers hvis "spalshpage", hvor man kan oprette bruger og logge ind

	'''

	return render_template('bestil.html')
