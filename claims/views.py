from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import Claim
from .forms import ClaimForm

def index(request):
    return render(request, 'claims/homepage.html', {'user': request.user})

def create_user(request):
    print(request.POST)
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
    return render(request, 'claims/profile.html')

@login_required
def file_claim(request):
    if request.method == 'POST':
        form = ClaimForm(request.POST, request.FILES)

        if form.is_valid():          
            claim = form.save(commit=False)
            claim.created_by = request.user
            claim.save()

            return redirect('profile')
            #     claim = Claim.objects.create(
            #         full_name = ,
            #         email = , 
            #         mobile_number = , 
            #         vehicle_manufacture_year = , 
            #         vehicle_model = ,
            #         vehicle_number = , 
            #         date_and_time_of_accident = , 
            #         accident_location = , 
            #         type_of_loss = , 
            #         description_of_loss = , 
            #         police_report_lodged = , 
            #         anybody_injured = , 
            #         photo = , 
            #         document_in_pdf_format = , 
            # )
        else:
            print(form.errors)
    else:
        form = ClaimForm()

    return render(request, 'claims/file_claim.html', {'form':form})
