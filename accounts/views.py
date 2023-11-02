from django.shortcuts import render

def test(request):
    return render(request , 'password_reset.html')
# Create your views here.

