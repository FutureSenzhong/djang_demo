from django.shortcuts import render


def photo(request):
    if request.method == 'GET':
        return render(request, 'show_time/share.html')
