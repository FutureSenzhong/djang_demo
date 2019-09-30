from django.shortcuts import render


def life(request):
    if request.method == 'GET':
        return render(request, 'show_time/info.html')
