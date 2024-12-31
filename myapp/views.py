from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return render(request, 'HTML/hello_world.html') # Refer to parent folder than file name. I.E. CSS/Filename.css