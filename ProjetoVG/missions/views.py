# missions/views.py
from django.shortcuts import render

def missions_list(request):
    return render(request, "missions/list.html")
