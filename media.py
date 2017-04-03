import webbrowser

class bands():
    def __init__(self,title,band_description,poster_image_url,trailer_youtube):
        self.title = title
        self.band_description = band_description
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
