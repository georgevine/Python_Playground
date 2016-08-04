import numpy as np
import wave, math

#audio sampling rate in hz
sRate = 44100
#total number of samples
nSamples = sRate * 5
#create numpy array of amplitude values for a 220hz sin wave based on the sin-wave equation
x = np.arange(nSamples)/float(sRate)
vals = np.sin(2.0*math.pi*220.0*x)
#scale amplitude values to 16 bit and convert into strings to be written to file
data = np.array(vals*32767, 'int16').tostring()
#create wav file
f = wave.open('sine220.wav', 'wb')
f.setparams((1, 2, sRate, nSamples, 'NONE', 'uncompressed'))
f.writeframes(data)
f.close()
