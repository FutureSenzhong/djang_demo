from django.shortcuts import render


def about(request):
    if request.method == 'GET':
        return render(request, 'show_time/about.html')
