from flask import Blueprint, url_for, render_template, request, redirect, flash, g
from models import Person

bns_blueprint = Blueprint('bns_leader',__name__,template_folder='templates')


def object_list(template,query):

	if request.args.get('q'):
		search = request.args['q']
		query = query.filter(Person.name.contains(search))
	return render_template(template,persons=query)


@bns_blueprint.route('/')
def bns_home():

	persons = Person.query.filter(
		Person.person_type == "Business Leader"
		).order_by(Person.created_timestamp.asc())
	return object_list('bns_home.html',persons)


@bns_blueprint.route('/detail/')
def detail():

	return render_template('bns_detail.html')
	


