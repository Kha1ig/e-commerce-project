from django.contrib.auth import get_user_model
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from register.tools.tokens import account_activation_token
from django.core.mail import send_mail

User=get_user_model()

def send_email(user_id, site_address):

    user = User.objects.filter(id=user_id).first()
    from_email = settings.EMAIL_HOST_USER
    recipient = user.email
    subject = 'Please confirm your email'
    context = {
        'user': user,
        'site_address': site_address,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),

    }

    body = render_to_string('emails/email-confirmation.html', context)
    mail_message = EmailMessage(subject=subject, to=[recipient], from_email=from_email, body=body)

    mail_message.content_subtype = 'html'
    mail_message.send(fail_silently=True)


def send_forget_password_mail(email , token ):
    subject = 'Your forget password link'
    message = f'Hi , click on the link to reset your password http://127.0.0.1:8000/register/login/change-password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True



