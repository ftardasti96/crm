from django.shortcuts import render, redirect
from .models import PersonalData
from .forms import PersonalForm

# Create your views here.
def new_customer(request):
    form = PersonalForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request,'customerform/thanks.html')
    return render(request, 'customerform/index.html',{'form':form})

