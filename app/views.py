from django.shortcuts import render
from .models import Blog
from blog.settings import main
# Create your views here.

def home(request):
    blog  = Blog.objects.all()
    try:  
        main()
    except:
        pass
    return render(request,'index.html',{'blogs':blog})