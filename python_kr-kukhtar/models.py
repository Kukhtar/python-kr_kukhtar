from flask_sqlalchemy import SQLAlchemy
from extensions.database import db
from marshmallow_enum import EnumField
from flask_marshmallow import Marshmallow
from marshmallow import Schema, post_load
from marshmallow_sqlalchemy import ModelSchema

ma = Marshmallow()

class Agreement(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	code = db.Column(db.String)
	name = db.Column(db.String)
	deadline = db.Column(db.String)
	price = db.Column(db.Integer)
	types = db.Column(db.String)

	def __repr__(self):
		return '<Agreement %r>' % self.id 



class AgreementSchema(ma.ModelSchema):
#    priority = EnumField(priorityEnum, by_value=True)

    @post_load
    def make_case(self, data):
        return Agreement(**data)

    class Meta:
        model = Agreement

