from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def home(request): return render(request, 'home.html')
def understanding(request): return render(request, 'understanding.html')
def resources(request): return render(request, 'resources.html')

def contact(request):
    if request.method == 'POST':
        ContactMessage.objects.create(
            name=request.POST.get('name', ''),
            email=request.POST.get('email', ''),
            category=request.POST.get('category', 'other'),
            message=request.POST.get('message', '')
        )
        messages.success(request, 'Thank you! Your message has been sent and saved.')
        return redirect('contact')
    return render(request, 'contact.html')
