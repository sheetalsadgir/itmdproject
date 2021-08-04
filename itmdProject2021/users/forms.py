from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.safestring import mark_safe


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class StatisticsForm(forms.Form):
    graphs = [
        ('bar', 'Bar Graph'),
        ('pie', 'Pie Chart'),
        ('line', 'Line Chart'),
        ('scatter', 'Scatter Plot'),
    ]

    crimes = [

        ('top5Five', 'Top 5 crimes Analysis'),
        ('domesticRatio', 'Domestic vs Non-Domestic Violence Ratio'),
        ('arrestRatio', 'Arrests/Non-Arrest Ratio !'),
        ('top5Block', 'Crimes Ratio by Top 5 blocks near me!'),
        ('totalThefts', 'Total Thefts between Jan 2019 - Dec 2019!'),
    ]

    graph = forms.CharField(label=mark_safe('Select Chart Type <br/>'),
                            widget=forms.RadioSelect(choices=graphs), required=False)

    crimeTypes = forms.CharField(label=mark_safe('Select Crime Analysis Report <br/>'),
                                 widget=forms.Select(choices=crimes), max_length=50, required=False)
