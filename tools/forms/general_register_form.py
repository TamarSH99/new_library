from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, ValidationError, Email
from ..models.user_model import User

class GeneralRegisterForm(FlaskForm):
    username = StringField('Username', validators=[
                            InputRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[
                            InputRequired(), Length(min=5, max=20)])
    password = PasswordField('Password', validators=[
                             InputRequired(), Length(min=8, max=20)])
    is_admin = BooleanField('is_admin')
    submit = SubmitField('Create User')
    
    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            flash('That username already exists. Please choose a different one.')
            raise ValidationError('That username already exists. Please choose a different one.')
        
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            flash('Email already exists')
            raise ValidationError('Email already exists')
