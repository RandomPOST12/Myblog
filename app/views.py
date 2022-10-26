from django.shortcuts import render
from .models import Blog
from blog.settings import main
# Create your views here.

def home(request):
    blog  = Blog.objects.all()
    main()
    return render(request,'index.html',{'blogs':blog})