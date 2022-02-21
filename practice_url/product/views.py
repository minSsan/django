from django.shortcuts import render

def productlist(request):
    return render(request, 'productlist.html')