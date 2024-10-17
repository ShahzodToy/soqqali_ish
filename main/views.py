from django.shortcuts import render, redirect
from .models import Portfolio, ClientFeedback
from .forms import ContactForm
from django.contrib import messages


def main_home(request):
    portfolio = Portfolio.objects.all()
    clients = ClientFeedback.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('main')  # Redirect to a success page or home page
    else:
        form = ContactForm()
    return render(request, 'index.html',{'portfolio':portfolio,'clients':clients})