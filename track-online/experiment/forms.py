from django import forms
from django.db import models
from .models import Info
    #Info,Details

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__'
        exclude = ('submission_date',)
        labels = {'name':'What is the name of your experiment?',
                  'submitter':'Submitted by',
                  'exp_type':'What kind of experiment is it? (For example picture naming, 2afc, etc.)',
                  'exp_link':'What is the link to your experiment?',
                  'exp_tool':'Which tool did you use?',
                  'participant_find': 'Was it easy or hard to find participants for this experiment?',
                  'participant_in_week': 'How many participants signed up, approximately, in 1 week?',
                  'participant_total':'How many participants did you test in total?',
                  'satisfactory':'Did the experiment run to your satisfaction?',
                  'technical_issues':'If not, which technical issues were encountered?',
                  'technical_exclusions':'Which proportion of data did you have to exclude for technical reasons?',
                  'pp_exclusions':'Approximately, which proportion of data did you have to exclude due to participant error, non-compliance with instructions, etc.?',
                  'outcome':'Were you overall happy with the quality of the data? Are they publishable?',
                  'comments':'Do you have any other comments?',
                  }

#class DetailsForm(forms.ModelForm):
#    exp_type = forms.CharField(max_length=100)
#    exp_link = forms.URLField()
#    exp_tool = forms.CharField(max_length=50)
#    participant_find = forms.CharField(max_length=6, widget=forms.Select(choices=Details.FINDING_OPTIONS))
#    participant_in_week = forms.IntegerField()
#    participant_total = forms.IntegerField()
#   satisfactory = forms.CharField(max_length=6, widget=forms.Select(choices=Details.SATISFACTION_OPTIONS))
#    technical_issues = forms.CharField(widget=forms.Textarea)
#   technical_exclusions = forms.IntegerField()# Percentage
#  pp_exclusions = forms.IntegerField()#Percentage
#    outcome = forms.CharField(widget=forms.Textarea)
#    comments = forms.CharField(widget=forms.Textarea)
#    class Meta:
#        model = Details
#        fields = '__all__'
