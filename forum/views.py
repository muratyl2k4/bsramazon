from django.shortcuts import render

def tests(request):
    from .models import Subject

    print(Subject.objects.get(id=1).count_comments())
    return render( request , 'forum_home.html')
    # Create your tests here.
