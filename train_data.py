import pickle as cPickle
import numpy as np
from scipy.io.wavfile import read
from sklearn.mixture import GaussianMixture 
from speakerfeatures import extract_features

source   = "file_wav/"
dest = "models/"
train_file = "file_wav.txt"        
file_paths = open(train_file,'r')

count = 1
features = np.asarray(())
for path in file_paths:    
    path = path.strip()   
    print (path)
    
    
    sr,audio = read(source + path)
    
    # extract 40 dimensional MFCC & delta MFCC features
    vector   = extract_features(audio,sr)
    
    if features.size == 0:
        features = vector
    else:
        features = np.vstack((features, vector))
    # when features of 10 files of speaker are concatenated, then do model training
    if count == 10:
        gmm = GaussianMixture(n_components = 16, covariance_type='diag',n_init = 3)
        gmm.fit(features)
        
        # dumping the trained gaussian model
        picklefile = path.split("/")[0]+".gmm"
        cPickle.dump(gmm,open(dest + picklefile,'wb'))
        print ('+ modeling completed :',picklefile)    
        features = np.asarray(())
        count = 0
    count = count + 1