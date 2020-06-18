from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# excel calc를 위한 Module
import pandas as pd

# Create your views here.
def excelCalcDo(request):
    inpt_file = request.FILES['fileInput']  # only get filePath
    
    # typeChange file to pd
    # 오류시 pip install xlrd
    df = pd.read_excel(inpt_file, sheet_name="Sheet1", header=0)
    
    grade_dic = {}
    total_row_num = len(df.index)

    for i in range(total_row_num)

    return HttpResponse("excelCalcDo Testing!")