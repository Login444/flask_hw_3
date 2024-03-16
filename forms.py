from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class SignInForm(FlaskForm):
    user_name = StringField('Name', validators=[DataRequired()])
    user_lastname = StringField('Lastname', validators=[DataRequired()])
    user_email = StringField('Email', validators=[DataRequired(), Email()])
    user_password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=8)])