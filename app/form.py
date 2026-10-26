from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,DateField
from wtforms.validators import DataRequired,Email,Length,Optional

class RegistrationForm(FlaskForm):
    name = StringField("Username",validators=[DataRequired(message="Name is required")])
    email = StringField("Email",validators=[DataRequired(message="Email is required for registration"),Email(message="Email is not valid")])
    password = PasswordField("Password",validators=[DataRequired(message="Password is required"),Length(min=6,message="Length should be atleast 5")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    name = StringField("Username",validators=[DataRequired(message="Name is required")])
    password = PasswordField("Password",validators=[DataRequired(message="Password is required"),Length(min=6,message="Length should be atleast 5")])
    submit = SubmitField("Login")

class EditForm(FlaskForm):
    date = DateField("Date",validators=[Optional()])
    title = StringField("title")
    save = SubmitField("Save Changes")