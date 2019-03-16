from django.core.mail import send_mail

def send_notification(subject, message, email):
    send_mail(subject, message, 'developert02@gmail.com', email, fail_silently=False)