import numpy as np
from match import freq1_from_ogg_path
import os
import sys

class Training(object):
    output_folder = "../model/"

    def __init__(self, path, fn):
        self.file_paths = [path + fname for fname in os.listdir(path) if fname.endswith(".ogg")]
        self.output_file = self.output_folder + fn
        print (self.file_paths)
        print (self.output_file)

    def train(self):
        while (self.file_paths != []):
            fname = self.file_paths.pop()
            freq1 = freq1_from_ogg_path(fname)
            with open(self.output_file, 'a') as f:
                f.write(fname + "|" + " ".join(map(str, freq1)) + "\n")
            print (fname + " done")


if __name__ == "__main__":
    t = Training(sys.argv[1], sys.argv[2])
    t.train()
