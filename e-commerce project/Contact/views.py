from django.shortcuts import render, redirect
from .models import Contact_info
from .forms import ContactForm
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def contact(request):
    Contact_information = Contact_info.objects.all()

    forum = ContactForm()
    if request.method == 'POST':
        forum = ContactForm(data=request.POST)
        if forum.is_valid():
            forum.save()
        return redirect(reverse('index:index'))
    
    context = {
        'forum': forum,
        'Contact_information': Contact_information
    }
    

    return render(request, 'contact.html', context=context)