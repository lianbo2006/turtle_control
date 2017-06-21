from django.shortcuts import render, redirect, HttpResponse
from app.models import Sound
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import Context, Template

# Create your views here.
def index(request):

    context = {}
    return render(request,'index.html',context)

def index_register(request):
    if request.method == "GET":
        form = UserCreationForm

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')

    context = {}
    context['form'] = form
    return render(request, 'register.html', context)

def index_login(request):
    page_next = request.GET.get("next")

    if request.method=='GET':
        form=AuthenticationForm
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            if page_next :
                return redirect(to=page_next)
            else :
                return redirect(to="index")

    context = {}
    context['form'] = form
    return render(request, 'login.html', context)

@login_required(login_url='login')
def control_panel_t(request):
    context = {}
    return render(request, 'control_panel_t.html', context)

@login_required(login_url='login')
def control_panel_d(request):
    context = {}
    return render(request, 'control_panel_d.html', context)
