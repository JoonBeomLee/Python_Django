from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from shareRes_app.models import *

# SMTP Module
from sendEmail_app.hidden import SMTP_INFO
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create your views here.
def sendEmail(request):
    checked_rsts = request.POST.getlist('checks')
    receiver = request.POST['inputReceiver'] 
    title = request.POST['inputTitle']
    content = request.POST['inputContent']

    mail_html = f"<html><body>"\
                f"<h1>맛집 추천</h1>"\
                f"<p> {content} <br />"\
                f"본 사이트에서 추천한 맛집은 다음과 같습니다.</p><br /><br />"

    for rst in checked_rsts:
        rst_obj = restaurant.objects.get(id=rst)
        mail_html += f"<h2>{rst_obj.rst_name}</h2>"\
                     f"<h3>* 관련 링크 <p>{rst_obj.rst_link}</p></h3><br/>"\
                     f"<h3>* 상세 내용 <p>{rst_obj.rst_content}</p></h3><br/>"\
                     f"<h3>* 관련 키워드 <p>{rst_obj.rst_keyword}</p></h3><br/><br/>"

    mail_html += "</body></html>"

    # SMTP
    try:
        SMTP_ID, SMTP_PWD = SMTP_INFO()
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(SMTP_ID, SMTP_PWD)
        msg = MIMEMultipart('alternative')
        msg['Subject'] = title
        msg['From'] = SMTP_ID
        msg['To'] = receiver
        mail_html = MIMEText(mail_html, 'html')
        msg.attach(mail_html)
        server.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
        server.quit()

        # success
        return render(request, 'sendSuccess.html')
    except:
        # fail
        return render(request, 'sendFail.html')