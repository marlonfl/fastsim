import os
import random
import soundfile as sf
import subprocess
import scipy.io.wavfile as scw
import time
import numpy as np

def lower_vol(song):
    return song * random.uniform(0.1, 0.8)

def short_clip(song):
    l = len(song)
    print ("got here too")
    start = random.randint(0, int(l*0.89))
    end = start + int(0.1*l)
    b = song[start:end]
    return b

def long_clip(song):
    l = len(song)
    start = random.randint(0, int(l*0.49))
    end = start + int(0.5*l)
    return song[start:end]

def downsample(song):
    return song[::2,::2]

if __name__ == "__main__":
    if not os.path.exists("../testfiles/original"):
        os.makedirs("../testfiles/original")
        os.makedirs("../testfiles/lower_vol")
        os.makedirs("../testfiles/short_clips")
        os.makedirs("../testfiles/long_clips")
        os.makedirs("../testfiles/downsampled")

    for fn in os.listdir("../trainfiles/"):
        data, sample_rate = sf.read("../trainfiles/" + fn)

        print (len(data))
        wav_name = fn.replace(".ogg", ".wav")

        scw.write("../testfiles/original/" + wav_name, sample_rate, data.astype(np.float32))
        time.sleep(4)
        os.system("oggenc -q 3 " + "../testfiles/original/" + wav_name)
        time.sleep(4)
        os.system("rm -f " + "../testfiles/original/" + wav_name)

        scw.write("../testfiles/lower_vol/" + wav_name, sample_rate, lower_vol(data).astype(np.float32))
        time.sleep(4)
        os.system("oggenc -q 3 " + "../testfiles/lower_vol/" + wav_name)
        time.sleep(4)
        os.system("rm -f " + "../testfiles/lower_vol/" + wav_name)

        scw.write("../testfiles/short_clips/" + wav_name, sample_rate, short_clip(data).astype(np.float32))
        time.sleep(4)
        os.system("oggenc -q 3 " + "../testfiles/short_clips/" + wav_name)
        time.sleep(4)
        os.system("rm -f " + "../testfiles/short_clips/" + wav_name)

        scw.write("../testfiles/long_clips/" + wav_name, sample_rate, long_clip(data).astype(np.float32))
        time.sleep(4)
        os.system("oggenc -q 3 " + "../testfiles/long_clips/" + wav_name)
        time.sleep(4)
        os.system("rm -f " + "../testfiles/long_clips/" + wav_name)

        scw.write("../testfiles/downsampled/" + wav_name, int(sample_rate/2), downsample(data).astype(np.float32))
        time.sleep(4)
        os.system("oggenc -q 3 " + "../testfiles/downsampled/" + wav_name)
        time.sleep(4)
        os.system("rm -f " + "../testfiles/downsampled/" + wav_name)
