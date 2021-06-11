from flask import Flask, render_template, url_for, request, flash, redirect, Blueprint
import platform, sys
from datetime import datetime
from .forms import Form
from flask_sqlalchemy import SQLAlchemy
from models import Agreement, AgreementSchema
from extensions.database import db

agreement_schema = AgreementSchema()
agreements_schema = AgreementSchema(many=True)

agreement_bp = Blueprint('agreement_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='')

@agreement_bp.route('/')
def index():
	return render_template('index.html')

@agreement_bp.route("/getall", methods=["GET"])
def get_tasks():
    all_agreements = Agreement.query.all()
    print(all_agreements)
    return AgreementSchema().dump(all_agreements[0])

@agreement_bp.route('/add', methods=['GET','POST'])
def form():
	f = Form()
	if request.method == 'POST':
 		if f.validate_on_submit():
 			a = Agreement(code=f.code.data, name = f.name.data, deadline = f.deadline.data, price = f.price.data, types = f.types.data )
 			db.session.add(a)
 			db.session.commit()
 			return redirect(url_for('agreement_bp.form'))
 		
	return render_template('add.html', form=f, pageTitle='Form')
if __name__ == "__main__":
	app.run(debug=True)
