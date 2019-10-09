from django.shortcuts import render


def photo(request):
    if request.method == 'GET':
        return render(request, 'show_time/../../templates/article/share.html')
