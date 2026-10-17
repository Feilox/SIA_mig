
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import MovieForm


def home(request):
    movies = Movie.objects.all()
    return render(request, 'InvApp/home.html', {'movies': movies})


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'InvApp/movie_list.html', {'movies': movies})


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'InvApp/movie_detail.html', {'movie': movie})


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()

    return render(request, 'InvApp/add_movie.html', {'form': form})


def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)

        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)

    return render(request, 'InvApp/edit_movie.html', {'form': form})


def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('movie_list')


def my_request(request):
    return render(request, 'InvApp/my_request.html')
