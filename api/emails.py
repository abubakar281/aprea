from django.core.mail import send_mail
import random
from django.conf import settings
from .models import user


def send_otp_via_mail(emai):
    subject = 'Your acoount verification email from APREA.'
    otp = random.randint(100000, 999999)
    message = f'your otp is:{otp}'
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [emai])
    user_obj = user.objects.get(email=emai)
    user_obj.otp = otp
    user_obj.save()