from django.shortcuts import render
from django.http import HttpResponse
from .models import covid_ind, covid_data_anal, data_base
# Create your views here.

def index(request):
      anal = covid_data_anal.objects.all()
      data = covid_ind.objects.all()
      my_dict = {'anals': anal, 'datas': data}
      return render(request, 'covid_app/index.html', context = my_dict)

def data(request):
      datas = data_base.objects.all()
      my_dict = {'datas': data}
      return render(request, 'covid_app/data.html', context = my_dict)