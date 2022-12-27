from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

"""
data={
    'movies':[
        {
            'id':5,
            'title':'jaws',
            'year':1669,
        },
        {
            'id':6,
            'title':'sharknado',
            'year':1600,
        },
        {
            'id':7,
            'title':'the meg',
            'year':2000,
        }
    ]
}"""
from .models import Movie
def movies(request):
    data=Movie.objects.all()
    return render(request,'movies/movies.html',{'movies':data})
def home(request):
    return HttpResponse('home page')
def detail(request,id):
    data=Movie.objects.get(pk=id)
    return render(request,'movies/detail.html',{'movie':data})
def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')
    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()#t
        return HttpResponseRedirect('/movies')
    return render(request,'movies/add.html')
def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exist')
    movie.delete()
    return HttpResponseRedirect('/movies')