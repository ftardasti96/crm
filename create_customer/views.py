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

def home(request):
    return render(request,'home/home.html')


def list(request):
    name = PersonalData.objects.order_by('id')
    return render(request,'list/all.html',{'name':name})


def detail(request,user_id):
    user = PersonalData.objects.get(pk=user_id)
    return render(request,'list/detail.html',{'user':user})