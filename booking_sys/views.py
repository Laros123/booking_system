from django.http import HttpResponseRedirect
from booking_sys.language import set_language

def base_set_language(request):
    previous_url = request.META.get('HTTP_REFERER')

    if previous_url:
        return HttpResponseRedirect(previous_url)
    else:
        return HttpResponseRedirect('/')

def russian(request):
    set_language(request, 'russian')
    return base_set_language(request)

def ukrainian(request):
    set_language(request, 'ukrainian')
    return base_set_language(request)

def english(request):
    set_language(request, 'english')
    return base_set_language(request)