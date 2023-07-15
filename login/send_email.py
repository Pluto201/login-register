import os
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoProject.settings'

if __name__ == '__main__':
    subject, from_email, to = '来自qs的测试邮件', 'handsomessq@sina.com', 'handsomessq@163.com'
    text_content = '活下去铁汁'
    html_content = '<p></p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


    # 0a0390e66f93c07c