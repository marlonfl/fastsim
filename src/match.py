import numpy as np
import sys
import scipy.io.wavfile as scw
import os
import scipy
from scipy.spatial.distance import euclidean
import soundfile as sf

SONG_POOL = ""
LIMIT = 0.25
N = 50

def stft(x, fftsize, overlap):
    """Returns short time fourier transform of a signal x
    """
    hop = int(fftsize / overlap)
    w = scipy.hanning(fftsize+1)[:-1]      # better reconstruction with this trick +1)[:-1]
    return np.array([np.fft.rfft(w*x[i:i+fftsize]) for i in range(0,len(x)-fftsize, hop)])


def sim(s1, s2):
    return euclidean(gen_model(s1), gen_model(s2))

def gen_model(song):
    fft1 = np.absolute(stft(song, 2048, 4)).mean(axis=0)
    fft1 /= max(fft1)
    return decimate(fft1.tolist(), N)

def freq1_from_ogg_path(path):
    raw = sf.read(path)[0]
    if raw.ndim > 1:
        raw = raw[:,1]
    fft = np.absolute(stft(raw, 32768, 2)).mean(axis=0)
    fft /= max(fft)
    return decimate(fft.tolist(), N)

def decimate(old, n):
    # lol
    n = n + 1
    per_bin = int(len(old)/n) + 1
    rest = per_bin*n - len(old)
    old = old + [0]*rest
    return [np.mean(old[i-per_bin:i]) for i in range(per_bin, len(old), per_bin)]

def load_model(path):
    temp = []
    with open(path, 'r') as f:
        temp = f.readlines()

    names = []
    vals = []
    for line in temp:
        s = line.split("|")
        names.append(s[0].split("/")[-1])
        vals.append([float(val) for val in s[1].split(" ")])

    return names, vals

def predict(model, song):
    distances = []
    for s in model:
        distances.append(euclidean(s, song))

    return distances.index(min(distances))


if __name__ == "__main__":
    sample = freq1_from_ogg_path(sys.argv[1])
    names, model = load_model("../model/" + sys.argv[2])

    print (names[predict(model, sample)])
    # path = sys.argv[1]
    # sample_rate, raw = scw.read(path)
    #
    #
    # matches = {}
    # for fn in os.listdir(SONG_POOL):
    #     score = sim(raw, scw.read(fn)[1])
    #     if score > LIMIT:
    #         matches[fn] = score
    #
    # sort = sorted(matches, key=matches.get)
    # print (sort)
