# ==============================================================
# Utility: Start Audio to HORUS
# ==============================================================

from scipy.io import wavfile
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ==============================================================
# Function: Show Audio Info
# ==============================================================

def show_info(aname, a, r):
    print('-----------------------------------------------------')
    print("Audio:", aname)
    print('-----------------------------------------------------')
    print("Rate:", r)
    print('-----------------------------------------------------')
    print("Shape:", a.shape)
    print("Dtype:", a.dtype)
    print("Min, Max:", a.min(), a.max())
    print('-----------------------------------------------------')
    plot_info(aname, a, r)

# ==============================================================
# Function: Plot Signal
# ==============================================================

def plot_info(aname, a, r):
    sTitle = f'Signal Wave - {aname} at {r} Hz'
    plt.title(sTitle)
    sLegend = []

    # Handle number of channels safely
    num_channels = a.shape[1]

    for c in range(num_channels):
        sLabel = f'Ch{c + 1}'
        sLegend.append(sLabel)
        plt.plot(a[:, c], label=sLabel)

    plt.legend(sLegend , loc='upper right')
    plt.xlabel('Samples')
    plt.ylabel('Amplitude')
    plt.show()

# ==============================================================
# 2-Channel Processing
# ==============================================================

sInputFileName = 'C:/image/sound1.wav'
print('=====================================================')
print('Processing :', sInputFileName)
print('=====================================================')

InputRate, InputData = wavfile.read(sInputFileName)

# Ensure 2D array
if InputData.ndim == 1:
    InputData = np.reshape(InputData, (-1, 1))

# Determine number of channels
if InputData.shape[1] == 1:
    sColumns = ['Ch1']
else:
    sColumns = ['Ch1', 'Ch2']

show_info("2 Channel", InputData, InputRate)

ProcessData = pd.DataFrame(InputData, columns=sColumns)
ProcessData.to_csv('C:/image/HORUS-Audio-2ch.csv', index=False)

# ==============================================================
# 4-Channel Processing
# ==============================================================

sInputFileName = 'C:/image/sound2.wav'
print('=====================================================')
print('Processing :', sInputFileName)
print('=====================================================')

InputRate, InputData = wavfile.read(sInputFileName)

if InputData.ndim == 1:
    InputData = np.reshape(InputData, (-1, 1))

show_info("4 Channel", InputData, InputRate)

ProcessData = pd.DataFrame(InputData, columns=['Ch1', 'Ch2', 'Ch3', 'Ch4'])
ProcessData.to_csv('C:/image/HORUS-Audio-4ch.csv', index=False)

# ==============================================================
# 6-Channel Processing
# ==============================================================

sInputFileName = 'C:/image/sound3.wav'
print('=====================================================')
print('Processing :', sInputFileName)
print('=====================================================')

InputRate, InputData = wavfile.read(sInputFileName)

if InputData.ndim == 1:
    InputData = np.reshape(InputData, (-1, 1))

show_info("6 Channel", InputData, InputRate)

ProcessData = pd.DataFrame(InputData, columns=['Ch1', 'Ch2', 'Ch3', 'Ch4', 'Ch5', 'Ch6'])
ProcessData.to_csv('C:/image/HORUS-Audio-6ch.csv', index=False)

# ==============================================================
# 8-Channel Processing
# ==============================================================

sInputFileName = 'C:/image/sound4.wav'
print('=====================================================')
print('Processing :', sInputFileName)
print('=====================================================')

InputRate, InputData = wavfile.read(sInputFileName)

if InputData.ndim == 1:
    InputData = np.reshape(InputData, (-1, 1))

show_info("8 Channel", InputData, InputRate)

ProcessData = pd.DataFrame(InputData, columns=['Ch1', 'Ch2', 'Ch3', 'Ch4', 'Ch5', 'Ch6', 'Ch7', 'Ch8'])
ProcessData.to_csv('C:/image/HORUS-Audio-8ch.csv', index=False)

# ==============================================================
print('=====================================================')
print('Audio to HORUS - Done')
print('=====================================================')
