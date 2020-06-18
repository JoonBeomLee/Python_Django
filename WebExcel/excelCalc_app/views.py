from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# download File
import os
from django.conf import settings

# upload model
from .models import *

# excel calc를 위한 Module
import pandas as pd

# upload시 저장시점 확인하기위함
from datetime import datetime

def excelResult(request):
    # 로그인 유지 중이라면
    if 'user_id' in request.session.keys():
        context = {
            'grade_calcualte_dic': request.session['grade_calculate_dic'],
            'email_domain_dic': request.session['email_domain_dic'],
        }

        # result 전달 후 삭제 데이터 중첩 방지
        del request.session['grade_calculate_dic']
        del request.session['email_domain_dic']
        
        return render(request, 'result.html', context)
    else:
        # 로그인 페이지 이동
        return redirect('signIn')

# Create your views here.
def excelCalcDo(request):
    inpt_file = request.FILES['fileInput']  # only get filePath
    
    # 파일 저장하기
    origin_file_name = inpt_file.name
    user_id = request.session['user_id']
    now_HMS = datetime.today().strftime('%H%M%S')
    file_upload_name = now_HMS+'_'+user_id+'_'+origin_file_name
    inpt_file.name = file_upload_name
    document = uploadFile(user_upload_file = inpt_file)
    document.save()

    # typeChange file to pd
    # 오류시 pip install xlrd
    df = pd.read_excel(inpt_file, sheet_name="Sheet1", header=0)
    
    grade_dic = {}
    total_row_num = len(df.index)
    for i in range(total_row_num):
        data = df.loc[i]
        if not data['grade'] in grade_dic.keys():
            grade_dic[data['grade']] = [data['value']]
        else:
            grade_dic[data['grade']].append(data['value'])
    # grade별 최소값 최대값 평균값 구하기
    grade_calculate_dic = {}
    for key in grade_dic.keys():
        grade_calculate_dic[key] = {}
        grade_calculate_dic[key]['min'] = min(grade_dic[key])
        grade_calculate_dic[key]['max'] = max(grade_dic[key])
        grade_calculate_dic[key]['avg'] = float(sum(grade_dic[key]))/len(grade_dic[key])
    # 결과 출력
    grade_list = list(grade_calculate_dic.keys())
    grade_list.sort()
    for key in grade_list:
        print("# grade:",key)
        print("min:",grade_calculate_dic[key]['min'],end='')
        print("/ max:",grade_calculate_dic[key]['max'],end='')
        print("/ avg:",grade_calculate_dic[key]['avg'],end='\n\n')
    
    # 이메일 주소 도메인별 인원 구하기
    email_domain_dic = {}
    for i in range(total_row_num):
        data = df.loc[i]
        email_domamin = (data['email'].split("@"))[1]
        if not email_domamin in email_domain_dic.keys():
            email_domain_dic[email_domamin] = 1
        else:
            email_domain_dic[email_domamin] += 1

    grade_calculate_dic_to_session = {}
    for key in grade_list:
        grade_calculate_dic_to_session[int(key)] = {}
        grade_calculate_dic_to_session[int(key)]['max'] = float(grade_calculate_dic[key]['max'])
        grade_calculate_dic_to_session[int(key)]['avg'] = float(grade_calculate_dic[key]['avg'])
        grade_calculate_dic_to_session[int(key)]['min'] = float(grade_calculate_dic[key]['min'])
    request.session['grade_calculate_dic'] = grade_calculate_dic_to_session
    request.session['email_domain_dic'] = email_domain_dic
    
    return redirect('excelResult')

def downloadFile(request):
    path = request.GET['path']
    file_path = os.path.join(settings.MEDIA_ROOT, path)

    # 경로가 맞다면
    if os.path.exists(file_path):
        binary_file = open(file_path, 'rb')
        response = HttpResponse(binary_file.read(), content_type="application/liquid; charset=utf8")

        return response
    
    else:
        context={
            'message':"파일이 없거나 경로가 잘못됬습니다."
        }
        return render(request, 'error.html', context)
