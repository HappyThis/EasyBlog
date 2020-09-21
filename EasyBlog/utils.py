from hashlib import md5

from EasyBlog.my_singnals import send_email_signal


def send_email(emailto, title, content):
    send_email_signal.send(
        send_email.__class__,

        emailto=emailto,
        title=title,
        content=content)


def get_md5(str):
    m = md5(str.encode('utf-8'))
    return m.hexdigest()
