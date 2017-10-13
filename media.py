import webbrowser


class Media():
    """A model of a movie"""

    def __init__(self, movie_title, poster_image, trailer_youtube,
                 movie_rating):
        """
        Initialize title, poster image, youtube trailer
        and rating attributes
        """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating

    def show_trailer(self):
        """Open movie youtube trailer"""
        webbrowser.open(self.trailer_youtube_url)
