from django.shortcuts import render
from django import forms

class MyForm(forms.Form):
    fullname = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=5)

def formview(request):
    if request.method=='POST':
        form=MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['fullname']
            age = form.cleaned_data['age']
            x=1
            return render(request , 'subscribed.html',{'name':name,'x':x})
    else:
        form=MyForm()
    return render(request, 'form.html', {'form': form})