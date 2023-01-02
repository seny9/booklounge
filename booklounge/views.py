from django.shortcuts import render

def bookloungehome(request):

    return render(request, 'booklounge/bookloungehome.html')


def login(request):

    return render(request, 'booklounge/login.html')


def signup(request):

    return render(request, 'booklounge/signup.html')


def my(request):

    return render(request, 'booklounge/mypage.html')


def introduce(request):

    return render(request, 'booklounge/introduce.html')