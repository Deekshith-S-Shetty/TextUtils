from django.http import  HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request) :
    djtext = request.POST.get("texts","default")
    removepunc = request.POST.get("removepunc",'off')
    removespace = request.POST.get("removespace",'off')
    uppercase = request.POST.get("uppercase",'off')
    removelinesn = request.POST.get("removelines",'off')
    punctuations = '''()[]{}:;"'.,></?!@#$%^&*_-=+'''

    if(removepunc == 'on'):
        rtext = ''
        for char in djtext:
            if char not in punctuations:
                rtext = rtext + char
        djtext = rtext

    if (removespace == 'on'):
        rtext = ''
        for index,char in enumerate(djtext):
            if djtext[index] ==" "  and djtext[index+1]==" ":
                pass
            else:
                rtext = rtext + char
        djtext = rtext

    if (uppercase == 'on'):
        rtext = ''
        for char in djtext:
            rtext = rtext + char.upper()
        djtext = rtext

    if (removelinesn == 'on'):
        rtext = ''
        for char in djtext:
            if char != "\n" and char !='\r':
                rtext = rtext + char
        djtext = rtext

    analyzer = {"texts":djtext}
    return render(request,"analyze.html",analyzer)