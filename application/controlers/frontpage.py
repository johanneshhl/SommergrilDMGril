 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from application import app, request, redirect, escape, session, url_for, db, render_template, g, flash
from application.database.database import userContact, newsLetterEmail

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


@app.route('/bestil/download')
def bestilDownload():

	if 'documents' in session:
		return render_template('pdfer.html')

	else: 
		return redirect(url_for('bestil'))






@app.route('/session/signup', methods=['POST'])
def signup():

	newUser = newsLetterEmail(request.form['email']) #opret bruger
		
	#indsæt User Objectet
	db.session.add(newUser)
	db.session.commit()

	return redirect(url_for('index'))



@app.route('/session/order', methods=['POST'])
def order():

	newUser = userContact(request.form['name'],request.form['email'],request.form['phonenumber']) #opret bruger
		
	#indsæt User Objectet
	db.session.add(newUser)
	db.session.commit()


	session['documents'] = True
	session.permanent = True


	return redirect(url_for('bestilDownload'))
