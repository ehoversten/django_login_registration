from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login_registration/index.html')

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
        return redirect('/')
    else:
        for error in results[1]:
            messages.add_message(request, messages.ERROR, error)
    return redirect('/')

def process_login(request):
    print("-"*25)
    print('', request.POST)
    print("-"*25)
    return redirect('/')
