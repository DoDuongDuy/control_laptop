import CreateRecord
from speakerfeatures import extract_features
import os
import pickle as cPickle
import numpy as np
from scipy.io.wavfile import read
import time
import webbrowser
import ctypes


#path to training data
def run():
    source   = "test/"   
    modelpath = "models/"
    test_file = "test.txt"
    file_paths = open(test_file,'r')

    gmm_files = [os.path.join(modelpath,fname) for fname in os.listdir(modelpath) if fname.endswith('.gmm')]

    models = []
    for i in range(len(gmm_files)):
        file = open(gmm_files[i], 'rb')
        models.insert(i, cPickle.load(file))

    speakers   = [fname.split("/")[-1].split(".gmm")[0] for fname in gmm_files]


    # Read the test directory and get the list of test audio files 
    print("Start.  ")
    last = []
    while True:
        test = CreateRecord.Record()
        test.createRecord("test.wav")

        path = "test.wav"
        sr,audio = read(path)
        vector   = extract_features(audio,sr)
            
        log_likelihood = np.zeros(len(models)) 
            
        for i in range(len(models)):
            gmm    = models[i] 
            scores = np.array(gmm.score(vector))
            log_likelihood[i] = scores.sum()
            
        winner = np.argmax(log_likelihood)
        
        if speakers[winner] == "motrinhduyet":
             webbrowser.get("C:/Program Files (x86)/Internet Explorer/iexplore.exe %s").open("http://Google.com.vn")
             break
        elif speakers[winner] == "excel":
            os.startfile('C:/Program Files (x86)/Microsoft Office/root/Office16/EXCEL.EXE')
            break    
        elif speakers[winner] == "khoamanhinh":
            ctypes.windll.user32.LockWorkStation()
            break
        # elif speakers[winner] == "tatnguon":
        #     os.system("shutdown /s /t 3600")
        #     break
        elif speakers[winner] == "24h":
            webbrowser.get("C:/Program Files (x86)/Internet Explorer/iexplore.exe %s").open("http://24h.com.vn")
            break
        elif speakers[winner] == "dung":
            break
            
    
        


