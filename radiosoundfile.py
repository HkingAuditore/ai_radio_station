import os
import random

import librosa
from pydub import AudioSegment

import PATH

import os
import openai

from ai_lib import AIMusicAnalysis, AiTTS


class RadioSoundFile:
    @staticmethod
    def scan_sounds(file_path):
        music = []
        for (_, _, files) in os.walk(file_path, topdown=True):
            music.append(files)
        return music

    music_list = scan_sounds(PATH.MUSIC_PATH)
    dj_list = scan_sounds(PATH.DJ_PATH)

    @staticmethod
    def get_random_sound(t):
        return RadioSoundFile.get_sound(RadioSoundFile.get_random_sound_path(t))

    @staticmethod
    def get_random_sound_path(t):
        if t == 'music':
            return os.path.join(PATH.MUSIC_PATH, random.choice(RadioSoundFile.music_list[0]))
        if t == 'dj':
            return os.path.join(PATH.DJ_PATH, random.choice(RadioSoundFile.dj_list[0]))

    @staticmethod
    def get_sound(path):
        return AudioSegment.from_file(path)





class Music:
    def __init__(self, path, use_intro=True):
        self.path = path
        self.audio = RadioSoundFile.get_sound(path)
        self.name =
        if use_intro:
            y, sr = librosa.load(self.path)
            tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
            beat_times = librosa.frames_to_time(beat_frames, sr=sr)
            AiTTS.init()
            anal = 'If you are a DJ and the next song you want to play is '+ str(len(self.audio) / 1000.0) + ', which contains ' + str(len(beat_times)) + ' beats, please introduce the song in the language of the DJ as much as possible'
            AIMusicAnalysis.init()
            gpt = AIMusicAnalysis.get_ai_text(anal)
            print(gpt[1:-1])
            AiTTS.init()
            self.intro = AiTTS.speak(gpt)
