from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from .forms import *
from django.forms import ModelForm
from django.views import generic
from .models import Activity
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout, login, authenticate


# views
def index(request):
    activities = Activity.objects.all()
    return render(request, 'index.html', {'activities' :activities})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('avatar')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


# map
@login_required
def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'maps.html',
                  {'mapbox_access_token': mapbox_access_token})


# activity page
def activity(request):
    return render(request, 'activity-page.html')


# about page
def about(request):
    return render(request, 'about.html')

# history page
def history(request):
    activities = request.user.profile.history.all()
    return render(request, 'history.html', {'activities' :activities})

def favourites(request):
    activities = request.user.profile.favourites.all()
    return render(request, 'favourites.html', {'activities' :activities})

def allActivities(request):
    activities = Activity.objects.all()
    return render(request, 'allactivities.html', {'activities' :activities})

class ActivityListView(generic.ListView):
    model = Activity


class ActivityDetailView(generic.DetailView):
    model = Activity
    form_class = SaveFavourite
    fields = ['id']
    login_required = True

    def get_object(self, **kwargs):
        obj = super().get_object()
        self.request.user.profile.history.add(obj)
        return obj


@login_required
def create_activity(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateActivity(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/all_activities')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateActivity()

    return render(request, 'create-activity-page.html', {'form': form})


# def longlat(request):
#     activity_list = Activity.objects.all()
#     context = {
#         'activity_list': activity_list
#     }
#     return render(request, 'longlat.html', context)


def avatar(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfileFormAvatar(request.POST, instance=request.user.profile)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/postcode')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfileFormAvatar()
    return render(request, 'registration/avatar.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'index.html')

def postcode(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfileFormPostcode(request.POST, instance=request.user.profile)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfileFormPostcode()
    return render(request, 'registration/enter-your-post-code.html', {'form': form})

def profile(request):
    profile = request.user.profile
    return render(request, 'registration/user-profile.html', {'profile': profile})


def savefave(request):
    if request.method == 'POST':
        form = SaveFavourite(request.POST)
        if form.is_valid():
            actid = form['id_id'].value()
            obj = Activity.objects.get(pk=actid)
            request.user.profile.favourites.add(obj)
        else:
            actid = ""
    return redirect('activities/%s' % actid)