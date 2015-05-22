import webbrowser

class Movie():
    '''Movie class is a class define a movie object including the title, storyline,
       poster image, and tralier.'''
    
    def __init__(self, movie_title, moive_storyline, poster_img, trailer_youtube):
        self.title = movie_title
        self.sotryline = moive_storyline
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
