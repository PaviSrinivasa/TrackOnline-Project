from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import Http404
from django.urls import NoReverseMatch

from .forms import InfoForm

from .models import Info

@login_required(login_url='/accounts/login/')
def home(request):
     expInfo = Info.objects.all();
     return render(request, 'home.html', {'expInfo': expInfo, })


@login_required(login_url='/accounts/login/')
def add(request):
    if request.method == 'POST':
        filled_form = InfoForm(request.POST)
        if filled_form.is_valid():
            obj = filled_form.save(commit=False)
            obj.submitter = request.user
            created_exp = filled_form.save()
            created_exp_pk = created_exp.id
            #new_name = filled_form.cleaned_data.get('name')
            note = 'Success!! The new experiment has been added!'
        else:
            note = 'The new experiment was not created, please try again!'
        new_form = InfoForm()
        expInfo = Info.objects.all()
        return render(request, 'home.html', {'note': note, 'expInfo': expInfo, 'created_exp_pk':created_exp_pk,})
        #return render(request, 'add.html', {'addform': new_form, 'note': note, 'created_exp_pk':created_exp_pk,})
    else:
        form = InfoForm()
        return render(request, 'add.html', {'addform': form})


@login_required(login_url='/accounts/login/')
def edit_exp(request, id):
    exp = Info.objects.get(pk=id)
    form = InfoForm(instance=exp)
    if exp.submitter == request.user.get_username():
        if request.method == 'POST':
            filled_form = InfoForm(request.POST, instance=exp)
            if filled_form.is_valid():
                filled_form.save()
                form = filled_form
                expInfo = Info.objects.all()
                note = 'The experiment has been updated!'
                return render(request, 'home.html', {'note':note,'expInfo': expInfo,'editform':form,'exp':exp})
                #return render(request, 'edit_exp.html', {'note':note,'editform':form,'exp':exp})
    else:
            note = 'Sorry! You do not have permission to edit this experiment!'
            return render(request, 'home.html', {'note':note,})
    return render(request, 'edit_exp.html', {'editform':form,'exp':exp})

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        exps = Info.objects.filter(name__icontains=searched)
        return render(request, 'search.html', {'searched':searched,'exps':exps})
    else:
        return render(request, 'search.html', {})

def show_exp(request,id):
    exp = Info.objects.get(pk=id);
    return render(request, 'show_exp.html', {
        'exp': exp
        })


