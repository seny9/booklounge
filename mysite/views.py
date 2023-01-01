from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render
from .models import MainContent

def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    # 딕셔너리 변환
    context = {'content_list': content_list} 
    return render(request, 'mysite/content_list.html', context)
    #'mysite/content_list.html'에 content_list 데이터 적용 후 html파일(템플릿) 리턴
