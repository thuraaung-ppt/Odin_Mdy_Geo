from flask import Blueprint, url_for, render_template, request, redirect, flash, g
from models import Person

cdt_blueprint = Blueprint('cdt_parties',__name__,template_folder='templates')

def object_list(template,query):

	if request.args.get('q'):
		search = request.args['q']
		query = query.filter(Person.name.contains(search))
	return render_template(template,persons=query)

@cdt_blueprint.route('/')
def cdt_home():

	persons = Person.query.filter(
		Person.person_type == "cdt_parties"
		).order_by(Person.created_timestamp.desc())

	return object_list('cdt_home.html',persons)

@cdt_blueprint.route('/detail/')
def detail():

	return render_template("cdt_detail.html")