from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# django Email module
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from .hidden import SMTP_INFO

# Create your views here.
def sendEmail(request):
    return HttpResponse("sendEmail, Testing!")

# sendEmail Function get parameters in user_app > views > signUpJoin
def send(receiverEmail, verifyCode):
    try:
        context = {
            'verifyCode':verifyCode
        }
        msg_html = render_to_string('email_form.html', context)

        SMTP_ID, SMTP_PWD = SMTP_INFO()

        msg = EmailMessage(
            subject="인증 코드 발송 메일",
            body = msg_html,
            from_email = SMTP_ID,
            bcc=[receiverEmail]
        )
        msg.content_subtype = 'html'
        msg.send()
        
        # send email success!
        return True
    except:
        # send email fail
        return False