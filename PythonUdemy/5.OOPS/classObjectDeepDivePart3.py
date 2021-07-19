# Doc Strings

class song:
    """Class to represent a song
    Attributes:
        title (str) : The title of the song 
        artist (Artist) : An artist object representing the songs creater
        duration (int) : The duration of the song in seconds. May be Zero
    """
    def __init__(self, title, artist, duration=0):
        """Song init method

        Args:
            title (str): Initialises the title attribute 
            artist (Artist): At Artist object representing the song creator
            duration (int, optional): Initial value for the 'duration' attribute. Defaults to 0.
        """
        self.title = title
        self.artist = artist
        self.duration = duration

if __name__ == '__main__':
    print(song.__doc__)
    '''
    Class to represent a song
    Attributes:
        title (str) : The title of the song
        artist (Artist) : An artist object representing the songs creater
        duration (int) : The duration of the song in seconds. May be Zero
    '''
    print(song.__init__.__doc__)
    '''
    Song init method

        Args:
            title (str): Initialises the title attribute
            artist (Artist): At Artist object representing the song creator
            duration (int, optional): Initial value for the 'duration' attribute. Defaults to 0.
    '''
