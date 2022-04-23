from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from register.forms import LoginForm, RegistrationForm
from django.contrib import messages
from register.tasks import send_email
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from register.tools.tokens import account_activation_token

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model, login as django_login, logout as django_logout
User = get_user_model()
# Create your views here.

def user_profile(request):
    user = User.objects.filter().first()

    context = {
        'user': user,
    }
    return render(request, 'user-profile.html', context)



def forgot_password(request):

    return render(request, 'forgot-password.html')

def login(request):

    forum = LoginForm()
    if request.method == 'POST':
        forum = LoginForm(request.POST)
        if forum.is_valid():
            email = forum.cleaned_data.get('email')
            password = forum.cleaned_data.get('password')
            user = authenticate(email = email, password=password)
            if user:
                django_login(request, user)
                messages.success(request,'You have successfully ')
                return redirect(reverse_lazy('index:index'))

    return render(request, 'login.html', {'forum': forum})

def logout(request):

    django_logout(request)
    return redirect(reverse_lazy('register:login'))

def register(request):

    form = RegistrationForm()
    if request.method == 'POST':
        form=RegistrationForm(data=request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.is_active = False
            user.save()
            site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST']  # https
            send_email(user_id=user.id, site_address=site_address)
    
    context= {'form': form}

    return render(request, 'register.html', context)

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Email is activated')
        return redirect(reverse_lazy('accounts:login'))
    elif user:
        messages.error(request, 'Email is not activated.')
        return redirect(reverse_lazy('accounts:register'))
    else:
        messages.error(request, 'Email is already activated')
        return redirect(reverse_lazy('accounts:register'))
