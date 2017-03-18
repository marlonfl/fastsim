import numpy as np
import sys
import scipy.io.wavfile as scw
import os
import scipy
from scipy.spatial.distance import euclidean

SONG_POOL = ""
LIMIT = 0.5
N = 200

def stft(x, fftsize, overlap):
    """Returns short time fourier transform of a signal x
    """
    hop = int(fftsize / overlap)
    w = scipy.hanning(fftsize+1)[:-1]      # better reconstruction with this trick +1)[:-1]
    return np.array([np.fft.rfft(w*x[i:i+fftsize]) for i in range(0,len(x)-fftsize, hop)])


def sim(s1, s2):
    fft1 = np.absolute(stft(s1, 32768, 2)).mean(axis=0)
    fft2 = np.absolute(stft(s2, 32768, 2)).mean(axis=0)
    fft1 /= max(fft1)
    fft2 /= max(fft2)
    ds1 = decimate(fft1.tolist(), N)
    ds2 = decimate(fft2.tolist(), N)
    return euclidean(ds1, ds2)

def decimate(old, n):
    # lol
    n = n + 1
    per_bin = int(len(old)/n) + 1
    rest = per_bin*n - len(old)
    old = old + [0]*rest
    return [np.mean(old[i-per_bin:i]) for i in range(per_bin, len(old), per_bin)]

if __name__ == "__main__":
    raw1 = scw.read(sys.argv[1])[1][:,1]
    raw2 = scw.read(sys.argv[2])[1][:,1]
    print ("normal: " + str(sim(raw1, raw2)))
    print ("vol change:" + str(sim(raw1*0.1, raw2)))
    print ("s1 selber: " + str(sim(raw1, raw1)))
    print ("s2 selber: " + str(sim(raw2, raw2)))
    print ("s1 ausschnitt: " + str(sim(raw1, raw1[0:int(len(raw1)/2)])))
    print ("s2 ausschnitt: " + str(sim(raw2, raw2[0:int(len(raw2)/2)])))

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