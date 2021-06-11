from flask import Flask

from .agreement.views import  agreement_bp
from extensions.database import db
# from models import Task,Category	


def create_app():
	app = Flask(__name__)
	app.config.from_object('config') #налаштування з файлу config.py
	app.register_blueprint(agreement_bp, url_prefix='/')

	# database.init_app(app)
	db.init_app(app)
	with app.app_context():
		db.create_all()
	return app
