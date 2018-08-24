from flask import Blueprint, url_for, render_template, request, redirect, flash, g
from models import Person

cele_blueprint = Blueprint('cele',__name__,template_folder='templates')


def object_list(template,query):

	if request.args.get('q'):
		search = request.args['q']
		query = query.filter(Person.name.contains(search))
	return render_template(template,persons=query)



@cele_blueprint.route('/')
def cele_home():
	return render_template('cele_list.html')

@cele_blueprint.route('/<person_type>')
def cele_list(person_type):

	# persons = Person.query.filter_by(person_type = person_type)

	persons = Person.query.filter(
		Person.person_type == person_type
		).order_by(Person.created_timestamp.desc())


	return object_list('cele_home.html',persons)