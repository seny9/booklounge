from django.shortcuts import render

def bookclubhome(request):
    bookclub_listdata = Bookclub.objects.order_by('-pub_date')
    # 딕셔너리 변환
    list = {'bookclub_list': bookclub_listdata}
    return render(request, 'bookclublounge/bookclubhome.html', list)

def bookclub(request):
    return render(request, 'bookclublounge/company_info.html')

