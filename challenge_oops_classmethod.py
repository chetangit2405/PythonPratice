class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    # ➤ Define from_string() here
    @classmethod
    def from_string(cls, movie_str):
        title, director, year = movie_str.split("|")
        return cls(title, director, int(year))

    def display(self):
        print(f"{self.title} ({self.year}) by {self.director}")

# ➤ Test
movie = Movie.from_string("Inception|Nolan|2010")
movie.display()