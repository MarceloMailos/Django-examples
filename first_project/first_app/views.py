from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    ttn_dictionary = {'ttn_textForBody': "value for the ttn_textForBody"}
    return render(request, 'first_app/index.html', ttn_dictionary)
    # return HttpResponse("Hello World !")