from django.shortcuts import render

def formview(request):
    return render(request,'form.html')