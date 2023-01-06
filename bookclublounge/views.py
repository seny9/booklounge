from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Bookclub

def bookclubhome(request):
    bookclub_list = Bookclub.objects.order_by('-pub_date')
    # 딕셔너리 변환
    list = {'bookclub_list': bookclub_list} # {'템플릿에서 읽을 변수명':정렬한 변수명}
    return render(request, 'bookclublounge/bookclubloungehome.html', list)

def showBookclub(request, name):
    if name is not None:
        bookclub = Bookclub.objects.get(name=name)
        return render(request, 'bookclublounge/bookclub.html', {'bookclub': bookclub})
