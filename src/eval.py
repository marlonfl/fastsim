from train import Training
import match
import sys


if __name__ == "__main__":
    names, model = load_model("../model/" + sys.argv[1])
    t = Training("../trainfiles/", sys.argv[1])
    t.train()

    accs = {}
    for folder in os.listdir("../testfiles/"):
        correct = 0
        fnames = os.listdir("../testfiles/" + folder + "/")
        for fn in fnames):
            s = match.freq1_from_ogg_path("../testfiles/" + folder + "/" + fn)
            pred = names[match.predict(model, s)]
            if pred == fn:
                correct += 1
                print (fn + " classified as " + pred + " [CORRECT]")
            else:
                print (fn + " classified as " + pred + " [NOT CORRECT]")

        accs[folder] = correct/len(fnames)


    print ("______________________________")
    for deg in accs.keys():
        print (deg + ": " + str(accs[deg]))

    print ("Total: " + str(sum(accs.values())/len(accs)))
