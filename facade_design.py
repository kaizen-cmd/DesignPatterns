class PlayMusic:

    def play_song(self):
        print("Playing music")


class PlayGame:

    def play_game(self):
        print("Playing game")


class DownloadMovie:

    def download_movie(self):
        print("Downloading movie")


class Computer:

    def __init__(self):

        self.play_music = PlayMusic()
        self.play_game = PlayGame()
        self.download_movie = DownloadMovie()

    def use_computer(self):

        self.play_music.play_song()
        self.play_game.play_game()
        self.download_movie.download_movie()


c = Computer()
c.use_computer()
