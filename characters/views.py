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
import plotly as py 


# def CharacterView(request):
#     return render(request, 'createcharacter.html')

class CharacterView(generic.FormView):
    template_name = 'characters/createcharacters.html'
    form_class = CharacterForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())
