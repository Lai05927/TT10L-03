import pygame

# Initialize the Pygame mixer
pygame.mixer.init()

def play_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(0)  # display only once

def stop_music():
    pygame.mixer.music.stop()