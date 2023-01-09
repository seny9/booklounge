from django.shortcuts import render

def bookloungehome(request):
    context = {}

    # user세션 존재한다면 넘겨주기, 없다면 공백
    context['nickname'] = request.session.get('nickname', '')

    return render(request, 'booklounge/bookloungehome.html', context)


# def login(request):
#     if request.method == 'POST': #요청이 post인 경우
#         form = userForm(request.POST) #요청 데이터를 userForm객체에 넣는다
#         if form.is_valid(): #폼의 데이터가 유효하다면
#             form.save() #폼의 데이터를 db의 필드별로 저장
#     else:
#             form = userForm() #post요청이 아닌 경우 단순 폼 출력
#
#     return render(request, 'booklounge/login.html', {'form': form})
#
#
# def signup(request):
#     if request.method == 'POST': #요청이 post인 경우
#         form = signupForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#             form = signupForm() #post요청이 아닌 경우 단순 폼 출력
#
#     return render(request, 'booklounge/signup.html', {'form': form})


def my(request):

    return render(request, 'booklounge/mypage.html')


def introduce(request):

    return render(request, 'booklounge/introduce.html')