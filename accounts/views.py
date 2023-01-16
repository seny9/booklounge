from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

from accounts.models import User
from accounts.forms import SignupForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)  # 사용자 인증
            login(request, user)
        return redirect('/booklounge')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html')
    elif request.method == "POST":
        context = {}

        email = request.POST.get('email')
        password = request.POST.get('password')

        # 로그인 체크하기
        loginCheck = User.objects.filter(email=email, password=password).first()
        print(email + '/' + password)
        print(loginCheck)

        # 이메일, 비밀번호 입력창 공백

        # 올바른 입력
        if loginCheck is not None:

            # 로그인 정보 세션 저장
            request.session['email'] = email
            request.session['nickname'] = loginCheck.nickname

            context['email'] = email
            context['nickname'] = loginCheck.nickname
            context['message'] = loginCheck.nickname + "님이 로그인하셨습니다."
            return render(request, 'booklounge/bookloungehome.html', context)

        # 회원정보 없음
        else:

            context['message'] = "회원정보가 없습니다"
            return render(request, 'accounts/login.html', context)
# def signup(request):
#     if request.method == "GET":
#         return render(request, 'accounts/signup.html')
#     elif request.method == "POST":
#         context = {}
#         email = request.POST["email"]
#         nickname = request.POST["nickname"]
#         password = request.POST["password"]
#         passwordconfirm = request.POST["passwordconfirm"]
#         name = request.POST["name"]
#
#
#         # 이메일, 닉네임, 비밀번호 입력창 공백입력
#         if email=='' or password=='':
#             context['message'] = "필수 항목을 입력하세요."
#             return render(request, 'accounts/signup.html', context)
#
#         # 이메일 형식 벗어남
#
#         # 닉네임 형식 벗어남
#         # 비밀번호 형식 벗어남
#         # 이메일 중복
#         signupEmail = User.objects.filter(email=email)
#         if signupEmail.exists():
#             context['message'] = "사용중인 이메일입니다."
#             return render(request, 'accounts/signup.html', context)
#
#         # 닉네임 중복
#         # 비밀번호 입력과 비밀번호 확인 입력이 다름
#
#         else:
#             User.objects.create(
#                 email=email, nickname=nickname, password=password, usage_flag='y')
#             context['message'] = name + "님 회원가입 되었습니다."
#             return render(request, 'booklounge/bookloungehome.html', context)
        





def logout(request):
    request.session.flush()
    return redirect('/booklounge/')
