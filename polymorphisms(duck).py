"""

class vehicle:
    def move(self):
        pass

class car(vehicle):
    def move(self):
        print("The Car drives on the road")

class  boat(vehicle):
        def move(self):
            print("The boat sails on water")

class plane(vehicle):
        def move(self):
            print( "The plane flies in the sky")


vechicles=[car() , boat() , plane()]

for vechicle in vechicles:
    vechicle.move()
"""

from abc import ABC ,abstractmethod

class MediaPlayer(ABC):
    @abstractmethod
    def play(self):
        pass

class AudioPlayer(MediaPlayer):
    def play(self):
        print("Playing an audio file...")

class VideoPlayer(MediaPlayer):
    def play(self):
        print("Playing a video file...")

class StreamingPlayer(MediaPlayer):
    def play(self):
        print("Streaming media online...")


mediaplay=[AudioPlayer(),VideoPlayer(),StreamingPlayer()]

for mediaplaying in mediaplay:
    mediaplaying.play()