To get MFCC, compute the DCT on the mel-spectrogram.

MFCC is a very compressible representation, often using just 20 or 13 coefficients instead of 32-64 bands in Mel spectrogram. (BW: gammatone filter bank use e.g. 64 or 128 bands.) The MFCC is a bit more decorrelarated, which can be beneficial with linear models like Gaussian Mixture Models. With lots of data and strong classifiers like Convolutional Neural Networks, mel-spectrogram can often perform better.

There are two steps:
+ 1. Take logs of Mel spectrogram.
+ 2. Compute DCT on logs.

To understand the answer to this question you should first understand how MFCC is computed. First you compute the mel frequency specrogram, log it then take the discrete cosine transform. The last stage is a linear operation so can be absorbed into the first layer of the neural network. So really the main difference is whether you log the mel frequency specrogram or not (and maybe power normalise). In terms of performance, the mel filterbank is slightly ahead, but not by much. There are two philosophical advantages, firstly it is often good to get the DNN to learn complex representations and not impose them, and secondly I've always hated the log, it's quite reasonable to have no power in a frequency range, so you end up fudging things to avoid ln(0).
