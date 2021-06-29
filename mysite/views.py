#i created this-@akshay
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #params = {'name':'Akshay','place':'mars'}
    return render(request,'index.html')
def analyze(request):
    op=request.POST.get('text','default')
    removepunc= request.POST.get('removepunc', 'off')
    fullcaps= request.POST.get('fullcaps', 'off')
    newlineremove=request.POST.get('newlineremove','off')
    xtraspaceremove= request.POST.get('xtraspace', 'off')

    if removepunc=="on":
        anal=""
        punctuations='''!/[-[\]{}()*+?.,\\^$|#]/,&"";;'''
        for i in op:
            if i not in punctuations:
                anal+=i
        params={'process':'remove punctuations','anal_text':anal}
        op=anal
    if fullcaps=='on':
        upper=""
        for char in op:
            upper+=char.upper()
        params={'process':'Changed to upper Case','anal_text':upper}
        op=upper

    if newlineremove =='on':
        new=""
        for char in op:
            if char!="\n" and char!="\r":
                new+=char
        params={'process':'Removed new line','anal_text':new}
        op=new

    if xtraspaceremove =='on':
        space=""
        for index,char in enumerate(op):
            if op[index]==" " and op[index+1]==" ":
                pass
            else:
                space+=char
        params={'process':'Removed space','anal_text':space}
        op=space

    elif(removepunc!="on" and xtraspaceremove!="on" and newlineremove!="on" and fullcaps!="on"):
        error="Select An Option"
        params={'out':error}
        return render(request,'error.html',params)
    return render(request, 'analyze.html', params)