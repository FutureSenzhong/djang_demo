from django.shortcuts import render


def comment(request):
    if request.method == 'GET':
        return render(request, 'show_time/list.html')
