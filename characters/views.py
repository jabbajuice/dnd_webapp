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

@login_required
def CharacterView(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            new_character = form.save(commit=False)
            new_character.user = request.user
            new_character.save() 
    else:
        form = CharacterForm()
    return render(request, 'createcharacter.html', {"form":form})



# def dashboard(request):
#     users = UserProfile.objects.all()
#     x_data = [user.user.username for user in users]
#     y_data = [user.date_joined for user in users] 
#     fig = px.scatter(x=x_data, y=y_data)
#     plot_div = fig.to_html(full_html=False)
#     context = {'plot_div': plot_div}
#     return render(request,'dashboard.html',context)


 