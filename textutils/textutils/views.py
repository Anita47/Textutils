# I have created thhis file--Anita
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def analyze(request):
    print('run')
    #get the text
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    if removepunc=="on":
        punctuations = '''!()-[]{};:'""\,<>./?2#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        params={'purpose':'removepunc','analyzed_text':analyzed}

        return render(request,'analyze.html',params)
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'change to uppercase','analyzed_text':analyzed}
        djtext=analyzed

    if newlineremover=='on':
        analyzed=""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed=analyzed+char
        params={'purpose':'new line removr','analyzed_text':analyzed}
        djtext=analyzed


    if extraspaceremover=='on':
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index]=="" and djtext[index+1]=="":
                pass
            else:

                analyzed=analyzed+char
        params={'purpose':'extra space remove','analyzed_text':analyzed}
    if(removepunc!="on"and fullcaps!="on"  and  newlineremover!='on' and extraspaceremover!='on'):
        return HttpResponse("Plese select any operation")
    return render(request, 'analyze.html', params)


