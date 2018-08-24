from flask import Blueprint, url_for, render_template, request, redirect, flash, g
from models import Person

modern_blueprint = Blueprint('modern_figures',__name__,template_folder='templates')


@modern_blueprint.route('/')
def modern_home():

	persons = Person.query.filter_by(person_type = "modern_figures")
	return render_template('modern_home.html',persons=persons)


@modern_blueprint.route('/detail/')
def detail():
	return render_template("modern_detail.html")