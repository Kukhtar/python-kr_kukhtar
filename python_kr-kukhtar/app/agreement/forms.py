# відповідні імпорти класів  і полів форм, валідаторів
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

#Імплементувати контактну форму
class Form(FlaskForm):
	code = StringField('Шифр договору: ', validators=[DataRequired()])
	name = StringField('Ім\'я організації: ', validators=[DataRequired()])
	deadline = StringField('Термін: ', validators=[DataRequired()])
	price = StringField('Сума договору: ', validators=[DataRequired()])
	types = SelectField("Вид договору: ", choices=[
    	("односторонній", "односторонній"), 
    	("двосторонній", "двосторонній"), 
    	("багатосторонній", "багатосторонній")]) 

