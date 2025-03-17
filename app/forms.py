from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    # submit = SubmitField('Login')

# class UploadForm(FlaskForm):
#     file = FileField('Upload an Image', validators=[
#         FileRequired(), 
#         FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
#     ])
#     submit = SubmitField('Upload File')
