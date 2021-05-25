from django.shortcuts import render
from django.http import Http404
from django.urls import NoReverseMatch

from .forms import InfoForm

from .models import Info


# Info, Details

def home(request):
    expInfo = Info.objects.all();
    return render(request, 'home.html', {
        'expInfo': expInfo
        })


def add(request):
    if request.method == 'POST':
        filled_form = InfoForm(request.POST)
        if filled_form.is_valid():
            created_exp = filled_form.save()
            created_exp_pk = created_exp.id
            #new_name = filled_form.cleaned_data.get('name')
            note = 'Success!! The new experiment has been added!'
        else:
            note = 'The new experiment was not created, please try again!'
        new_form = InfoForm()
        expInfo = Info.objects.all();
        return render(request, 'home.html', {'note': note, 'expInfo': expInfo, 'created_exp_pk':created_exp_pk,})
        #return render(request, 'add.html', {'addform': new_form, 'note': note, 'created_exp_pk':created_exp_pk,})
    else:
        form = InfoForm()
        return render(request, 'add.html', {'addform': form})


def edit_exp(request, id):
    exp = Info.objects.get(pk=id)
    form = InfoForm(instance=exp)
    if request.method == 'POST':
        filled_form = InfoForm(request.POST,instance=exp)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'The experiment has been updated!'
            return render(request, 'edit_exp.html', {'note':note,'editform':form,'exp':exp})
    return render(request, 'edit_exp.html', {'editform':form,'exp':exp})
