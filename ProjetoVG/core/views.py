from django.shortcuts import render
#from django.http import HttpResponse

def home(request):
    #return HttpResponse("<h1> Bem Vindos à Venture Gotchi!</h1>")
    context={
        'nome_usuario':'Gotcher',
        'atividades':['Desafio_01','Desafio_02','Desafio_03']
    }
    return render(request,'home.html',context)

# Create your views here.
