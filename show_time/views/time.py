from django.shortcuts import render


def time(request):
    if request.method == 'GET':
        return render(request, 'show_time/time.html')
