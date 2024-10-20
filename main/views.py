from django.shortcuts import render, redirect
from .models import Portfolio, ClientFeedback, Service,Team
from .forms import ContactForm
from django.contrib import messages


def main_home(request):
    portfolio = Portfolio.objects.all()
    clients = ClientFeedback.objects.all()
    services = Service.objects.all()[:3]
    teams = Team.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('main')  # Redirect to a success page or home page
    else:
        form = ContactForm()
    return render(request, 'main_home.html',{'portfolio':portfolio,'clients':clients,'services':services,'teams':teams})

def portfolio_view(request,pk):
    portfolio = Portfolio.objects.get(id = pk) 
    portfolio_other = Portfolio.objects.exclude(id = pk)
    return render(request, 'portfolios.html', {'portfolio': portfolio,'portfolio_other':portfolio_other})

def team_view(request, pk):
    team = Team.objects.get(id = pk)  
    team_other = Team.objects.exclude(id = pk)
    return render(request, 'team_detail.html', {'team': team,'team_other':team_other})


def service_view(request):
    serivces = Service.objects.all()

    return render(request, 'service_page.html',{'serivces':serivces})