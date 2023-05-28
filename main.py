import os
import random
import threading
import time

import pyaudio as pyaudio
import pygame
from pathlib import Path
import simpleaudio
from pydub.playback import _play_with_simpleaudio

from pydub import AudioSegment
from pydub.playback import play
import librosa
from radiosoundfile import RadioSoundFile, Music

import PATH




def init_pydub():
    AudioSegment.converter = "ffmpeg.exe"
    AudioSegment.ffprobe = "ffprobe.exe"


if __name__ == '__main__':
    init_pydub()

    song = Music(RadioSoundFile.get_random_sound_path('music'))
    dj = Music(song.intro,use_intro=False)

    stream = song.audio.fade_in(2000).fade_out(3000)

    mixed = stream.overlay(dj.audio.fade_in(1000).fade_out(1000) - 5, position=5000, gain_during_overlay=-8)

    t = threading.Thread(target=play, args=(mixed,), daemon=True)
    t.start()
    print(1)
    t.join()
    print(2)

    # pygame.mixer.pre_init()
    # pygame.mixer.init()
    # pygame.init()
    #
    # pygame.mixer.music.load(path2)
    # pygame.mixer.music.set_volume(0.3)
    # pygame.mixer.music.play(loops=-1)
    # pygame.mixer.Channel(0).play(pygame.mixer.Sound(path0))
    # pygame.mixer.Channel(1).play(pygame.mixer.Sound(path1))
