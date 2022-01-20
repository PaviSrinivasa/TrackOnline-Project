from django.db import models
from datetime import datetime

class Info(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=30, blank=True)
    submission_date = models.DateField(default=datetime.now)
    FINDING_OPTIONS = [('HARD', 'HARD'), ('MEDIUM', 'MEDIUM'),('EASY','EASY')]
    SATISFACTION_OPTIONS = [('YES','YES'), ('NO','NO')]
    exp_type = models.CharField(max_length=100)
    exp_link = models.CharField(max_length=180)
    exp_tool = models.CharField(max_length=50)
    participant_find = models.CharField(max_length=6, choices=FINDING_OPTIONS, blank=False)
    participant_in_week = models.IntegerField(null=False)
    participant_total = models.IntegerField(null=False)
    satisfactory = models.CharField(max_length=6, choices=SATISFACTION_OPTIONS, blank=False)
    technical_issues = models.TextField()
    technical_exclusions = models.IntegerField()# Percentage
    pp_exclusions = models.IntegerField()#Percentage
    outcome = models.TextField() #TextField
    comments = models.TextField()

    def __str__(self):
        return self.name
