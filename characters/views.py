from django.shortcuts import render
from .models import Player_Characters, UserProfile
from django.views import generic
from django.views import generic
from django.shortcuts import redirect, reverse, render
from django.contrib.auth import logout, login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import CharacterForm
import plotly.graph_objs as go 
import pandas as pd
import csv

@login_required
def CharacterView(request):
    form = CharacterForm(request.POST or None)
    return render(request, 'createcharacter.html', {"form":form})

# class CharacterView(generic.FormView):
#     template_name = 'characters/createcharacters.html'
#     form_class = CharacterForm

    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     return HttpResponseRedirect(self.get_success_url())

# def plot(request):
#     data = pd.read_csv('Lending-Company-Total-Price.csv', delimiter=',')
#     bar_chart = go.Bar(x=data['LoanID'], y=data['TotalPrice'])
#     bar_fig = go.Figure(data=bar_chart)
#     bar_chart_show = bar_fig.show()
#     context = {'Plot_div':bar_chart_show()}
#     return render(request, 'dashboard.html', context)

# def dashboard(request):
#     with open('Lending-Company-Total-Price.csv') as csvfile:
#         reader = csv.reader(csvfile)
#         headers = next(reader)
#         data = list(reader) 

#         x_data = [row[2] for row in data]
#         y_data = [row[6] for row in data] 

#         trace = go.Scatter(
#             x=x_data,
#             y=y_data,
#             mode='markers'
#         )

#         layout = go.Layout(
#             title="my plot",
#             xaxis=dict(title=headers[2]),
#             yaxis=dict(title=headers[6])
#         )

#         fig = go.Figure(data=[trace], layout=layout)
#         fig_show = fig.show()
#         # plot_div = fig.to_html(full_html=False)
#         context = {'Plot_div':fig_show()}
#     return render(request,'dashboard.html',context)

 