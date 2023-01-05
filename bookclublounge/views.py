from django.shortcuts import render
from .models import Bookclub

def bookclubhome(request):
    bookclub_list = Bookclub.objects.order_by('-pub_date')
    # 딕셔너리 변환
    list = {'bookclub_list': bookclub_list} # {'템플릿에서 읽을 변수명':정렬한 변수명}
    return render(request, 'bookclublounge/bookclubhome.html', list)

def bookclub(request):
    return render(request, 'bookclublounge/company_info.html')

