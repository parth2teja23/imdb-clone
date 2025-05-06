from flask import Flask, jsonify, request
from data import movies
from models import Movie
from flask import render_template


app = Flask(__name__)

@app.route("/movies", methods=["GET"])
def get_movies():
    return jsonify([movie.to_dict() for movie in movies])

@app.route("/movies/<int:id>", methods=["GET"])
def get_movie(id):
    movie = next((m for m in movies if m.id == id), None)
    return jsonify(movie.to_dict()) if movie else ("Not found", 404)

@app.route("/movies", methods=["POST"])
def add_movie():
    data = request.get_json()
    movie = Movie(**data)
    movies.append(movie)
    return jsonify(movie.to_dict()), 201

@app.route("/movies/<int:id>", methods=["PUT"])
def update_movie(id):
    movie = next((m for m in movies if m.id == id), None)
    if not movie:
        return ("Not found", 404)
    data = request.get_json()
    movie.update(data)
    return jsonify(movie.to_dict())

@app.route("/movies/<int:id>", methods=["DELETE"])
def delete_movie(id):
    global movies
    movies = [m for m in movies if m.id != id]
    return ("Deleted", 204)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
