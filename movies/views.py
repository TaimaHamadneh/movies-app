from django.shortcuts import render


def index(request):
    context = {
        'movies': ['The Matrix', 'top gun', 'John Wick'],
    }
    return render(request, 'movies/index.html', context)

def about(request):
    return render(request, 'movies/about.html')

#app/templates/app/index.html
#movies/templates/movies/index.html