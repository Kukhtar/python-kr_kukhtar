from flask import Flask, render_template, url_for, request, flash, redirect
from app import app
import platform, sys
from datetime import datetime
from .forms import Form
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Agreement(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	code = db.Column(db.Integer)
	name = db.Column(db.String)
	deadline = db.Column(db.String)
	price = db.Column(db.Integer)
	types = db.Column(db.String)

	def __repr__(self):
		return '<Agreement %r>' % self.id 

with app.app_context():
    db.create_all()

@app.route('/')
def index():
	return render_template('index.html', data = data)

@app.route('/getall')
def getall():
	args = Agreement.query.all()
	return render_template('getall.html', args = args, len = len(args))

def getData():
	now = datetime.now()
	return ["User: " + str(request.headers.get('User-Agent')) , "Platform: " + str(platform.system()) + "Python version:" + str(sys.version_info[0]) + "   Time: " + str(now.strftime("%H:%M:%S"))]

@app.route('/add', methods=['GET','POST'])
def form():
	data = getData()
	f = Form()
	if request.method == 'POST':
 		if f.validate_on_submit():
 			a = Agreement(code=f.code.data, name = f.name.data, deadline = f.deadline.data, price = f.price.data, types = f.types.data )
 			db.session.add(a)
 			db.session.commit()
 			return redirect(url_for('form'))
 		
	return render_template('add.html', form=f, pageTitle='Form', data=data)
if __name__ == "__main__":
	app.run(debug=True)
