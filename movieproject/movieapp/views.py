from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import movieform
from .models import Movie


def index(request):
    obj=Movie.objects.all()
    return render(request,'index.html',{'res':obj})

def details(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':movie})

def addmovie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        detail=request.POST.get('detail')
        year=request.POST.get('year')
        img=request.FILES.get('img')
        movie=Movie(name=name,desc=desc,detail=detail,year=year,img=img)
        movie.save()
    return render(request,'addmovie.html')

def updatemovie(request,id):
    movie=Movie.objects.get(id=id)
    form=movieform(request.POST or None,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':movie})

def deletemovie(request,id):
    if request.method=="POST":
        movie=Movie.objects.get(id=id)
        if 'value1' in request.POST:
            movie.delete()
            return redirect('/')
        else:
            return render(request,'detail.html',{'movie':movie})

    return render(request,'delete.html')




