from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('Title', validators=[DataRequired('Title is necessary')])
    content = TextAreaField('Content', validators=[DataRequired('Content is necessary')])

class AnswerForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired('Content is necessary')])

class UserCreateForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', 'Incorrect Password')])
    password2 = PasswordField('Password Confirm', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired()])