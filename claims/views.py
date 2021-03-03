from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import Claim
from .forms import ClaimForm

def index(request):
    return render(request, 'claims/homepage.html', {'user': request.user})

def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('index')
    else:
        form = UserCreationForm()
        data = {
            'form': form,
            'signup': True
            }

        return render(request, 'claims/authentication.html', data)

@login_required
def profile(request):
    user = request.user
    claims = Claim.objects.filter(created_by=user)

    return render(request, 'claims/profile.html', {'claims': claims})

@login_required
def file_claim(request):
    if request.method == 'POST':
        form = ClaimForm(request.POST, request.FILES)

        if form.is_valid():          
            claim = form.save(commit=False)
            claim.created_by = request.user
            claim.save()

            return redirect('profile')
        else:
            print(form.errors)
    else:
        form = ClaimForm()

    return render(request, 'claims/file_claim.html', {'form':form})

@login_required
def edit_claim(request, id):
    single_claim = Claim.objects.get(pk=int(id))

    import datetime
    datetime_local_format = single_claim.date_and_time_of_accident.strftime("%Y-%m-%dT%H:%M")
    single_claim.date_and_time_of_accident = datetime_local_format

    if request.method == 'POST':
        form = ClaimForm(request.POST, instance=single_claim)
        if form.is_valid():

            # security measure for html code injection / amending url
            if form.cleaned_data['claim_approved'] == True:
                return redirect('profile')

            form.save()
            return redirect('profile')
    else:
        form = ClaimForm(instance=single_claim)

        data = {
            'form': form,
            'claim': single_claim
            }

        return render(request, 'claims/edit_claim.html', data)

@login_required
def delete_claim(request, id):
    single_claim = Claim.objects.get(pk=int(id))

    # # security measure for html code injection / amending url
    if single_claim.claim_approved == True:
        return redirect('profile')

    if request.method == 'POST':
        single_claim.delete()
        return redirect('profile')
    else: 
        return render(request, 'claims/delete_claim.html', {'claim': single_claim})