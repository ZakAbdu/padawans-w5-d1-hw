from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)


movies = {
    '1': {
        'title': 'Batman The Dark Knight',
        'year': '2008',
        'director': 'Christopher Nolan'
    },
    '2': {
        'title': 'The Pursuit of Happyness',
        'year': '2006',
        'director': 'Gabriele Muccino'
    },
    '3': {
        'title': 'Django Unchained',
        'year': '2012',
        'director': 'Quentin Tarantino'
    }
}

@app.route('/')
def hello():
    return '<h1>Hellon<h1>'

# Read
@app.get('/movie')
def get_movies():
    return { 'movies': list(movies.values()) }


# Create
@app.post('/movie')
def create_movie():
    movie_data = request.get_json()
    movies[uuid4()] = movie_data
    return { 'message': f'Movie: {movie_data["title"]} added to movies list' }, 201

# Update
@app.put('/movie/<movie_id>')
def update_movie(movie_id):
    try:
        movie = movies[movie_id]
        movie_data = request.get_json()
        movie |= movie_data
        return { 'message': f'{movie["title"]} updated' }, 202
    except KeyError:
        return { 'message': 'Invalid Movie' }, 400

# Delete
@app.delete('/movie/<movie_id>')
def delete_movie(movie_id):
    if movie_id in movies:
        movie = movies[movie_id]
        del movies[movie_id]
        return { 'message': f'{movie["title"]} has been deleted' }, 201
    else:
        return { 'message': 'Movie not found' }, 400

