
from flask_admin import Admin , AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView 
from flask_admin.contrib.fileadmin import FileAdmin
from wtforms.fields import SelectField, PasswordField

from app import app ,db 
from models import Person 

admin = Admin(app,'Site Admin')

class AdminModelView(ModelView):
	column_list = ['image_id','name','person_type','biography','created_timestamp']

	

admin.add_view(AdminModelView(Person,db.session))


