import django
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver

from EasyBlog import settings

send_email_signal = django.dispatch.Signal(
    providing_args=['emailto', 'title', 'content'])


@receiver(send_email_signal)
def send_email_signal_handler(sender, **kwargs):
    emailto = kwargs['emailto']
    title = kwargs['title']
    content = kwargs['content']

    msg = EmailMultiAlternatives(
        title,
        content,
        from_email=settings.EMAIL_HOST_USER,
        to=emailto)
    msg.content_subtype = "html"

    msg.send()
