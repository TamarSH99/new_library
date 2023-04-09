from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import check_password_hash
from ..models.user_model import User

class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[
                             InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')

    def check_account(self, extra_validators=None):
        if not super().validate():
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user is None or not check_password_hash(user.password, self.password.data):
            flash('Invalid username or password')
            return False
        return True
