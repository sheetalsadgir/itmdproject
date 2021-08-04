import pandas
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserRegisterForm, StatisticsForm
from . import plots
import pandas as pd

def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')


def statistics(request):
    context = {}
    chart = {}
    crimes_print = ''
    form = StatisticsForm(request.POST or None)
    if form.is_valid():
        # form.save()
        graph = form.cleaned_data.get('graph')
        crime_report = form.cleaned_data.get('crimeTypes')
        print('******* Plotting Graph of type: ******* ', graph)
        print('******* Plotting Graph for : ******* ', crime_report)

        if graph == '' or graph is None or crime_report is None or crime_report == '':
            messages.success(request, f'Please select available report and chart type from below selections.')
        elif graph == 'bar' and crime_report == 'top5Five':
            chart = plots.plotTopFiveCrimes('bar')
        elif graph == 'scatter' and crime_report == 'top5Five':
            chart = plots.plotTopFiveCrimes('scatter')
        elif graph == 'line' and crime_report == 'top5Five':
            chart = plots.plotTopFiveCrimes('line')
        elif graph == 'pie' and crime_report == 'top5Five':
            messages.success(request, f'Sorry but we dont have Pie Chart available for your selected report')

        elif graph == 'pie' and crime_report == 'arrestRatio':
            chart = plots.plotArrestsRatio()

        elif (graph == 'bar' or graph == 'line' or graph == 'scatter') and crime_report == 'arrestRatio':
            messages.success(request, f'Sorry but we dont have {graph} Chart available for your selected report')

        elif graph == 'pie' and crime_report == 'domesticRatio':
            chart = plots.plotDomesticRatio()

        elif (graph == 'bar' or graph == 'line' or graph == 'scatter') and crime_report == 'domesticRatio':
            messages.success(request, f'Sorry but we dont have {graph} Chart available for your selected report')

        elif graph == 'bar' and crime_report == 'top5Block':
            chart = plots.plotTopFiveCrimesByBlock('bar')
        elif graph == 'line' and crime_report == 'top5Block':
            chart = plots.plotTopFiveCrimesByBlock('line')
        elif graph == 'scatter' and crime_report == 'top5Block':
            chart = plots.plotTopFiveCrimesByBlock('scatter')
        elif graph == 'pie' and crime_report == 'top5Block':
            messages.success(request, f'Sorry but we dont have {graph} Chart available for your selected report')

        elif graph == 'bar' and crime_report == 'totalThefts':
            chart = plots.plotTheftByDates('bar')
        elif graph == 'line' and crime_report == 'totalThefts':
            chart = plots.plotTheftByDates('line')
        elif graph == 'scatter' and crime_report == 'totalThefts':
            chart = plots.plotTheftByDates('scatter')
        elif graph == 'pie' and crime_report == 'totalThefts':
            messages.success(request, f'Sorry, No Pie chart  available for your selected report')

    context['chart'] = chart
    context['form'] = form


    return render(request, 'users/statistics.html', context=context)
