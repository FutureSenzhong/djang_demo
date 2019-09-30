from django.shortcuts import render


def study(request):
    if request.method == 'GET':
        return render(request, 'show_time/fengmian.html')
