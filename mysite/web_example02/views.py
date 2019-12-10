from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Привет программисты.<br> Обещаю, до начала зимних каникул выучу django ;)</h1>")