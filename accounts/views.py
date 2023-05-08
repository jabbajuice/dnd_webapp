from django.views import generic
from django.shortcuts import redirect, reverse, render
from django.contrib.auth import logout, login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import UserForm, AuthForm, UserProfileForm, UserAlterationForm
from .models import UserProfile
from characters.models import Player_Characters
import plotly as py 
from django.shortcuts import render, get_object_or_404

class SignUpView(generic.FormView):
    template_name = "accounts/sign_up.html"
    form_class = UserForm
    success_url = '/account/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

class SignInView(generic.FormView):
    template_name = "accounts/sign_in.html"
    form_class = AuthForm
    success_url = '/account-dashboard/'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())


def sign_out(request):
	logout(request)
	return redirect(reverse('accounts:sign-in'))


@login_required
def AccountView(request):
    up = request.user.userprofile
    up_form = UserProfileForm(instance = up)
    context = {'form': up_form}

    if request.method == "POST":
        form = UserProfileForm(instance = up, data = request.POST)
        if form.is_valid:
            form.save()
            return redirect('/account-dashboard/')
    else:
        return render(request, 'accounts/account.html', context)


@login_required
def UserInfoView(request):
    user = request.user
    u_form = UserAlterationForm(instance = user)
    context = {'form': u_form}

    if request.method == "POST":
        form = UserAlterationForm(instance = user, data = request.POST)
        if form.is_valid:
            form.save()
            return redirect('/account-dashboard/')
    else:
        return render(request, 'accounts/dashboard.html', context)

@login_required
def dashboard(request):
    user_profile = request.user.userprofile
    characters = Player_Characters.objects.filter(UserID=user_profile.id)
    return render(request, 'accounts/dashboard.html',{'characters':characters})


def character_details(request,character_id):
    character = get_object_or_404(Player_Characters, pk=character_id)
    return render(request, 'accounts/detail.html',{'character':character})
