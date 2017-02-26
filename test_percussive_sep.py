import numpy as np

import librosa
import librosa.display

y, sr = librosa.load('woman_got_culture.wav', offset=40, duration=10)
D = librosa.stft(y)
D_harmonic, D_percussive = librosa.decompose.hpss(D)