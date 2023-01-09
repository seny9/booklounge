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
        bookclub = get_object_or_404(Bookclub, name=name)
        return render(request, 'bookclublounge/bookclub.html', {'bookclub': bookclub})

def login(request):
    if request.method == 'POST': #요청이 post인 경우
        form = userForm(request.POST) #요청 데이터를 userForm객체에 넣는다
        if form.is_valid(): #폼의 데이터가 유효하다면
            form.save() #폼의 데이터를 db의 필드별로 저장
    else:
            form = userForm() #post요청이 아닌 경우 단순 폼 출력

    return render(request, 'booklounge/login.html', {'form': form})
