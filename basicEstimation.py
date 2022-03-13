from functools import partial
from scipy.io.wavfile import read, write
# parsing .wav file

# def estimateWMatrix(m1,m2)
# Math here
# return W,confidenceNumber # estimates


# input parse .wavs -> m1,m2
# Call: estimate W
# Build signals [a,b] = W.[m1 m2]

# Write outputs a,b into .wavs


# TODO
# 1. Basic math part
# 2. Wav parsing
# 3. Three test cases 
    # a. (300 Hz,400 Hz) = (30,70) 
    # b. (300 Hz,400 Hz) = (70,30)
    # c. (300 Hz,400 Hz) = (100,0)  
    # d. (300 Hz,400 Hz) = (0,100)  
    # These cover relative amplitudes, what about phase delays?