from flask import Blueprint, url_for, render_template, request, redirect, flash, g
from models import Person
mb_blueprint = Blueprint('mb_pmt',__name__,template_folder='templates')


def object_list(template,query):

	if request.args.get('q'):
		search = request.args['q']
		query = query.filter(Person.name.contains(search))
	return render_template(template,persons=query)


@mb_blueprint.route('/')
def mb_home():
	persons = Person.query.filter(
		Person.person_type == "mb_pmt"
		).order_by(Person.created_timestamp.asc())
	return render_template('mb_home.html',persons=persons)


@mb_blueprint.route('/detail/')
def detail():
	return render_template('mb_detail.html')