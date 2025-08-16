import pygame
import datetime
import time
def call_alarm(alarm_time):

    play_music ="Alarm_song.mp3"
    is_running=True

    while is_running:
        current_time=datetime.datetime.now().strftime("%H : %M : %S")
        print(current_time)

        if current_time == alarm_time:
            print(" Wake Up !!! ")

            pygame.mixer.init()
            pygame.mixer.music.load(play_music)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False
        time.sleep(1)


if __name__ == "__main__":
    alarm = input("Enter the alarm(HH : MM : SS) : ")
    call_alarm(alarm)