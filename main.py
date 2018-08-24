from app import app,db 
import views
import models 
import admin

# from cfp.cfp_blueprint import cfp
# app.register_blueprint(cfp,url_prefix='/cfp/')

from bns_leader.bns_blueprint import bns_blueprint
app.register_blueprint(bns_blueprint,url_prefix='/bns/')

from cdt_parties.cdt_blueprint import cdt_blueprint
app.register_blueprint(cdt_blueprint,url_prefix='/cdt/')

from cele.cele_blueprint import cele_blueprint
app.register_blueprint(cele_blueprint,url_prefix='/cele/')

from mb_pmt.mb_blueprint import mb_blueprint
app.register_blueprint(mb_blueprint,url_prefix='/mb/')

from modern_figures.modern_blueprint import modern_blueprint
app.register_blueprint(modern_blueprint,url_prefix='/modern_figures/')

if __name__ == '__main__':
    app.run()
