import os
import random

import pyaudio as pyaudio
import pygame
from pathlib import Path

from pydub import AudioSegment
from pydub.playback import play

import PATH


def scan_music(path):
    music = []
    for (_, _, files) in os.walk(path, topdown=True):
        music.append(files)
    return music


if __name__ == '__main__':
    print(AudioSegment.ffmpeg)
    AudioSegment.converter = r"F:\\Developent\\AI\\AIRadio\\ai_radio_station\\ffmpeg-2023-05-25-git-944243477b-full_build\\bin\\ffmpeg.exe"
    AudioSegment.ffprobe = r"F:\\Developent\\AI\\AIRadio\\ai_radio_station\\ffmpeg-2023-05-25-git-944243477b-full_build\\bin\\ffprobe.exe"
    print(AudioSegment.ffmpeg)
    music_list = scan_music(PATH.MUSIC_PATH)
    path0 = os.path.join(PATH.MUSIC_PATH, random.choice(music_list[0]))
    path1 = os.path.join(PATH.MUSIC_PATH, random.choice(music_list[0]))
    path2 = os.path.join(PATH.MUSIC_PATH, random.choice(music_list[0]))
    print(path0)
    my_file = Path("F:\\Developent\\AI\\AIRadio\\Music\\01 - Victoria III (Official Game Soundtrack) - A Prospering Country.mp3")
    song = AudioSegment.from_mp3(my_file)

    play(song)

    # pygame.mixer.pre_init()
    # pygame.mixer.init()
    # pygame.init()
    #
    # pygame.mixer.music.load(path2)
    # pygame.mixer.music.set_volume(0.3)
    # pygame.mixer.music.play(loops=-1)
    # pygame.mixer.Channel(0).play(pygame.mixer.Sound(path0))
    # pygame.mixer.Channel(1).play(pygame.mixer.Sound(path1))
