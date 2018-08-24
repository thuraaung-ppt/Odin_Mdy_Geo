from app import app 
from flask import render_template , request
from config import Configuration
from models import Person 


def object_list(template,query):

	if request.args.get('q'):
		search = request.args['q']
		query = query.filter(Person.name.contains(search))
	return render_template(template,persons=query)


@app.route('/')
def home():

	# persons = Person.query.all()
	persons = Person.query.order_by(Person.created_timestamp.desc())
	return object_list('home.html',persons)



@app.route('/contact')
def contact():
	return render_template('contact.html')


@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/news')
def news():
	return render_template('latest.html')


@app.route('/detail/<slug>')
def detail(slug):

	person = Person.query.filter_by(slug=slug).first_or_404()
	return render_template('detail.html',person=person)


