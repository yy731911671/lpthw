class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    a = 123
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right here"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
print(happy_bday.a)

Song.a = 345

bulls_on_parade.sing_me_a_song()
print(happy_bday.a)
