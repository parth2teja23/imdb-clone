class Movie:
    id_counter = 1

    def __init__(self, title, year, genre):
        self.id = Movie.id_counter
        Movie.id_counter += 1
        self.title = title
        self.year = year
        self.genre = genre

    def to_dict(self):
        return {"id": self.id, "title": self.title, "year": self.year, "genre": self.genre}

    def update(self, data):
        self.title = data.get("title", self.title)
        self.year = data.get("year", self.year)
        self.genre = data.get("genre", self.genre)
