from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
    return render(request, 'appForms/index.html')

def formPage(request):
    form = forms.formName()
    if request.method == "POST":
        form = forms.formName(request.POST)
        if form.is_valid():
            print("Validation success")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])
        else:
            print("The submission is not valid")
    else:
        print("The method is not POST, it is " + request.method)
    return render(request, 'appForms/formPage.html', {'form':form})