import django_filters
from django.db.models import Q
from .models import *
from django_filters import DateFilter, CharFilter

class ExpFilter(django_filters.FilterSet):
    class Meta:
        model = Info
        fields = {
            'name':['icontains'],
            'submitter':['icontains'],
            'exp_type':['icontains'],
            'exp_tool':['icontains']
        }
