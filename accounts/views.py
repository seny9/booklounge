from django.shortcuts import render, redirect

from accounts.models import User

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

        # if rs.exists():
        if loginCheck is not None:

            #로그인 정보 세션 저장
            request.session['email'] = email
            request.session['nickname'] = loginCheck.nickname

            context['email'] = email
            context['nickname'] = loginCheck.nickname
            context['message'] = loginCheck.nickname + "님이 로그인하셨습니다."
            return render(request, 'booklounge/bookloungehome.html', context)

        else:

            context['message'] = "회원정보가 없습니다"
            return render(request, 'accounts/login.html', context)

def signup(request):
    if request.method == "GET":
        return render(request, 'accounts/signup.html')
    elif request.method == "POST":
        context = {}
        email = request.POST["email"]
        nickname = request.POST["nickname"]
        password = request.POST["password"]
        passwordConfirm = request.POST["passwordConfirm"]
        name = request.POST["name"]


        # 회원가입 이메일 중복체크
        signupEmail = User.objects.filter(email=email)
        if signupEmail.exists():
            context['message'] = "사용중인 이메일입니다."
            return render(request, 'accounts/signup.html', context)

        else:
            User.objects.create(
                email=email, nickname=nickname, password=password, usage_flag='y')
            context['message'] = name + "님 회원가입 되었습니다."
            return render(request, 'booklounge/bookloungehome.html', context)




def logout(request):
    request.session.flush()
    return redirect('/booklounge/')
