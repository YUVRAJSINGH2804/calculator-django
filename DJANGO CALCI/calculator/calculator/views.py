from django.shortcuts import render
from django.http import HttpResponse

def  index(request):
    return render(request,'index.html')

def answer(request):
    djnum1= request.GET.get('first_num','defaut')
    djnum2 = request.GET.get('second_num', 'defaut')
    answer1=request.GET.get('sum','off')


    djnum1=int(djnum1)
    djnum2=int(djnum2)
    if answer1=="on":
        o=djnum1+djnum2



    else:
        return HttpResponse('Error')

    parms = {'solution':o}
    return render(request,'sol.html',parms)

