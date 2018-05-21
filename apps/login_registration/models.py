from __future__ import unicode_literals
from django.db import models
from  django.core.validators import validate_email
from django.core.exceptions import ValidationError

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
        if not form['password']:
            errors.append("Password is required")
        if not form['pass_confirm']:
            errors.append("Confirmation is required")

        if not errors:
            print("x"*25)
            print("No Errors")
            print("x"*25)
            user = User.objects.create(f_name=form['f_name'], l_name=form['l_name'], email=form['email'], user_password=form['user_password'])
        # --- Returns a Tuple (no_errors_bool?, OBJECT)
            return (True, user)
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
        return "<User: {}| {} {} | {} : {}>".format(self.id, self.f_name, self.l_name, self.email, self.password)

    objects = UserManager()
