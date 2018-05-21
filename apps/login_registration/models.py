from __future__ import unicode_literals
from django.db import models
from  django.core.validators import validate_email
from django.core.exceptions import ValidationError
import bcrypt

def ValidateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

# import validatiors
from  django.core.validators import validate_email
from django.core.exceptions import ValidationError

class UserManager(models.Manager):

    def reg_validator(self, form):
        errors = []

        if not form['f_name']:
            errors.append("First name is required")
        if not form['l_name']:
            errors.append("Last name is required")
        if not form['email']:
            errors.append("Email is required")
        elif not ValidateEmail(form['email']):
            errors.append("Email must have valid format.")
        elif User.objects.filter(email=form['email']):
             errors.append("Account already exists.")
        if len(form['user_password']) < 5:
            errors.append("Password must have at least 5 characters.")
        if form['user_password'] != form['pass_confirm']:
            errors.append("Passwords do not match")

        if not errors:
            hashed_pass = bcrypt.hashpw(form['user_password'].encode(), bcrypt.gensalt())
            user = User.objects.create(f_name=form['f_name'], l_name=form['l_name'], email=form['email'], user_password=hashed_pass)
            return (True, user)
        else:
            return (False, errors)

    def loginValidator(self, form):

        errors = []

        if not form['email']:
            errors.append("Email required.")
        elif not ValidateEmail(form['email']):
            errors.append("Email must have valid format.")
        elif not User.objects.filter(email=form['email']):
             errors.append("Please register first")

        if len(form['user_password']) < 1:
            errors.append("Password cannot be empty")
        else:
            user = User.objects.filter(email=form['email'])
            if not bcrypt.checkpw(form['user_password'].encode(), user[0].user_password.encode()):
                errors.append("Password does not match password in database.")

        if not errors:
            return (True, user[0])
        else:
            return (False, errors)



# Create your models here.
class User(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<User: {}| {} {} | {} : {}>".format(self.id, self.f_name, self.l_name, self.email, self.user_password)

    objects = UserManager()
