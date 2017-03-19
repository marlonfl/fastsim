import os
import random
import soundfile as sf

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
    # os.makedirs("../testfiles/original")
    # os.makedirs("../testfiles/lower_vol")
    # os.makedirs("../testfiles/short_clips")
    # os.makedirs("../testfiles/long_clips")
    # os.makedirs("../testfiles/downsampled")

    for fn in os.listdir("../trainfiles/"):
        print (fn)
        data, sample_rate = sf.read("../trainfiles/" + fn)
        #sf.write("../testfiles/original/" + fn, data, sample_rate)
        print (data)
        d = lower_vol(data)
        print (sample_rate)
        sf.write("../testfiles/lower_vol/" + fn, d, sample_rate)
        sf.write("../testfiles/short_clips/" + fn, short_clip(data), sample_rate)
        sf.write("../testfiles/long_clips/" + fn, long_clip(data), sample_rate)
        sf.write("../testfiles/downsampled/" + fn, downsample(data), int(sample_rate/2))
