from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    EmailField,
    TextAreaField
)
from wtforms.validators import DataRequired, Email, Length, ValidationError


class RegistrationForm(FlaskForm):
    # to = StringField(
    #     "To",
    #     validators=[DataRequired(), Email()]
        
    # )
    
    # From = StringField(
    #     "From",
    #     validators=[DataRequired(), Email()]
        
    # )
    
    Receptiance = StringField(
        label="Recipients", description="Enter your receptiance with ( , ) separated",
        validators=[DataRequired(), Email()]
        
    )
    
    subject = StringField(
        "Subject", description="Enter the Subject",
        validators=[Length(min=5,max=50)]
        
    )
    
    body = StringField(
        "Message", description="Write the message you want to send",
        validators=[Length(min=5)]
        
    )
    
    
    submit = SubmitField("Send Mail", description="Send the mail")

# class NameForm(FlaskForm):
#     name = StringField("Enter Your Name: ", validators=[DataRequired()])
#     submit = SubmitField("Submit")

# class RegistrationForm(FlaskForm):
#     name = StringField(
#         "Full Name",
#         validators=[DataRequired()]
        
#     )
    
#     email = StringField(
#         "Email",
#         validators=[DataRequired(), Email()]
        
#     )
    
#     password = PasswordField(
#         "Password",
#         validators=[DataRequired()]  
#     )
    
#     gender = RadioField(
#         "Gender",
#         choices=[
#         ("M", "Male"),
#         ("F", "Female")
#         ]
#     )
    
#     country = SelectField(
#         "Country",
#         choices=[
#         ("np", "Nepal"),
#         ("in", "India")
#         ]
#     )
    
#     agree = BooleanField(
#         "I accept all the terms and conditions",
#         validators=[DataRequired()]
#     )
#     submit = SubmitField("Register")