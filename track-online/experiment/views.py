from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render,redirect
from django.http import Http404
from django.urls import NoReverseMatch
from django.contrib import messages
from .filters import ExpFilter

from .forms import InfoForm

from .models import Info

@login_required(login_url='/webexptrackaccounts/login/')
def home(request):
    expInfo = Info.objects.all().order_by('-id')
    if request.method == "GET":
        myFilter = ExpFilter(request.GET, queryset=expInfo)
        expInfo = myFilter.qs
        return render(request, 'home.html', {'expInfo': expInfo, 'myFilter': myFilter, })
    else:
        return render(request, 'home.html', {'expInfo': expInfo, })

@login_required(login_url='/webexptrackaccounts/login/')
def add(request):
    if request.method == 'POST':
        filled_form = InfoForm(request.POST)
        if filled_form.is_valid():
            obj = filled_form.save(commit=False)
            obj.submitter = request.user
            created_exp = filled_form.save()
            messages.success(request,'Success!! The new experiment has been added!')
            created_exp_pk = created_exp.id
        else:
            messages.error(request,'The new experiment was not created, please try again!')
        new_form = InfoForm()
        expInfo = Info.objects.all().order_by('-id')
        myFilter = ExpFilter(request.GET, queryset=expInfo)
        return render(request, 'home.html', {'expInfo': expInfo, 'created_exp_pk': created_exp_pk,'myFilter': myFilter, })
    else:
        form = InfoForm()
        return render(request, 'add.html', {'addform': form, })


@login_required(login_url='/webexptrackaccounts/login/')
def edit_exp(request, id):
    exp = Info.objects.get(pk=id)
    form = InfoForm(instance=exp)
    if exp.submitter == request.user.get_username():
        if request.method == 'POST':
            filled_form = InfoForm(request.POST, instance=exp)
            if filled_form.is_valid():
                filled_form.save()
                messages.success(request,'The experiment has been updated!')
                form = filled_form
                expInfo = Info.objects.all().order_by('-id')
                myFilter = ExpFilter(request.GET, queryset=expInfo)
                return render(request, 'home.html', {'expInfo': expInfo,'editform': form, 'exp':exp,'myFilter': myFilter, })
    else:
            messages.error(request,'Sorry! You do not have permission to edit this experiment!')
            expInfo = Info.objects.all().order_by('-id')
            myFilter = ExpFilter(request.GET, queryset=expInfo)
            return render(request, 'home.html', {'expInfo': expInfo, 'myFilter': myFilter, })
    return render(request, 'edit_exp.html', {'editform': form, 'exp': exp, })



