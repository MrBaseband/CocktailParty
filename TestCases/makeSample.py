# from fcntl import F_SEAL_GROW
# from socket import VM_SOCKETS_INVALID_VERSION
from matplotlib.pyplot import sca
import numpy as np
import argparse


# arguments to mix specific amplitude ratio and relative phase, else leave random if unspecified

f_max = 500 # max frequency in Hz
f_sample = 2*f_max # Nyquist rate

t_max = 10 # seconds
# Common timebase for all waveforms
T_sample = 1/f_sample
T_base = np.arange(0,t_max,T_sample)



# Synthesize two tones ---------------------------------------------------------------
# relativeAmplitudes = [0.25,0.75] # 
# relativePhase  = (np.pi/180)*[0,0] # degrees

# W-matrix
N = 2
# modify weights and delays below:
W_phaseDegMat = [[0,0],[0,0]] # delays in degrees
W_ampMat = [[1,0],[0,1]]

W = [[0,0],[0,0]] # dummy init
for m in range(N):
    for n in range(N): 
        W[m][n] = W_ampMat[m][n]*np.exp(1j*2*np.pi*(np.pi/180)*W_phaseDegMat[m][n])
print(W)
# 300 Hz complex tone
# tone_300Hz = relativeAmplitudes[0]*np.sin(1j*2*np.pi*300*T_base - relativePhase[0])
tone_300Hz = np.exp(1j*2*np.pi*300*T_base)

# 400 Hz complex tone
# tone_400Hz = relativeAmplitudes[1]*np.sin(1j*2*np.pi*400*T_base - relativePhase[1])
tone_400Hz = np.exp(1j*2*np.pi*400*T_base)

# combine the complex tones using W matrix (this matrix has complex entries, for amplitude AND phase)
result = []
for k in range(len(T_base)):
    result.append(np.real(np.matmul(W, [tone_300Hz[k],tone_400Hz[k]])))
    # print(result)

m1 = result[0]
m2 = result[1]

# Save the result as a .wav file --------------------------------------------------------
from scipy.io.wavfile import write
samplerate = 44100

data = m1
maxVal = np.max(data)
preconditioner = lambda x: np.int16(x/maxVal * 32767)
scaled = np.asarray(list(map(preconditioner, data)))
print(f'Printing scaled {scaled}')
write("m1.wav", samplerate, scaled)

# data = m2
# scaled = np.int16(data/np.max(np.abs(data)) * 32767)
# write("m2.wav", samplerate, scaled)