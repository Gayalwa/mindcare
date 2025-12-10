from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage

def home(request): return render(request, 'home.html')
def understanding(request): return render(request, 'understanding.html')
def resources(request): return render(request, 'resources.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip() or 'Anonymous'
        email = request.POST.get('email', '').strip() or 'No email'
        category = request.POST.get('category', 'Other')
        message_text = request.POST.get('message', '')

        # Save to database
        ContactMessage.objects.create(
            name=name, email=email, category=category, message=message_text
        )

        # Instant email to you
        send_mail(
            f"MindCare Kenya – {category} from {name}",
            f"Name: {name}\nEmail: {email}\nCategory: {category}\n\nMessage:\n{message_text}",
            settings.DEFAULT_FROM_EMAIL,
            ['arthurgayalwa@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, 'Thank you! Your message has been sent.')
        return redirect('contact')
    return render(request, 'contact.html')
