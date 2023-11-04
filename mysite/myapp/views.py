from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProfileForm
from django.views.generic import ListView
from .models import Profile

class ListProfileView(ListView):
    model = Profile
    template_name = 'profile_list.html'

def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = ProfileForm()
    return render(request, 'edit_profile.html', {'form': form})

def profile_update(request, pname):
    profile = Profile.objects.get(name=pname)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form, 'profile': profile})