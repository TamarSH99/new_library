from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError, Email
from ..models.user_model import User


class OnlyUserRegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), Length(min=6, max=80)])
    submit = SubmitField('Sign Up')

    
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            flash('That username already exists. Please choose a different one.')
            raise ValidationError('Username already exists')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            flash('Email already exists')
            raise ValidationError('Email already exists')

    def validate_confirm_password(self, field):
        if field.data != self.password.data:
            flash('Passwords must match')
            raise ValidationError('Passwords must match')
