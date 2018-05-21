from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    all_users = User.objects.all()
    context = {
        'all_users' : all_users
    }
    return render(request, 'login_registration/index.html', context)

def process_reg(request):
    print("-"*25)
    print('', request.POST)
    print("-"*25)
# --- send request.POST form data to be validated
# --- Call the registration validation method ---
    results = User.objects.reg_validator(request.POST)
    print("*"*25)
    print('\n')
    print('Errors: ', results)

# IF the new OBJECT in 'results' returns no errors to our errors LIST
    if results[0]:
        request.session['id'] = results[1].id
        request.session['f_name'] = results[1].f_name
        return redirect('/success')
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error)
    return redirect('/users')


def success(request):
    # print("x"*25)
    return render(request, 'login_registration/success.html')

def process_login(request):
    results = User.objects.loginValidator(request.POST)
    print("#"*25)
    print('Login Results: ', results)
    print("#"*25)

    if results[0]:
        request.session['id'] = results[1].id
        request.session['f_name'] = results[1].f_name
        return redirect('/success')
    else:
        for error in results[1]:
            messages.add_message(req, messages.ERROR, error, extra_tags='login')
        return redirect('/users')
