#Valentin Heinitz, 2016-10-20
#License: Public-Domain
# Attention, this software is provided as is, with no warranty!
# Use it on your own risk!
#
# Purpose:
# The script applies in random order speech-filters 1k-8k
# This effect should help in mental and speech development for children with autsm.
# I personally doubt it. However many parents spent big money for such "therapy".
# With this free software I hope to demystify this "complicated, scientifical" method.
# 
# Background: My son is autistic due tu vaccination. I'm in several autism parents-networks.
# We apply very promising method "CEASE Therapy" by Tinus Smits

import os
import sys
import re
import random

#Adjust the path for your PC
sox = "bin\\sox.exe"
ffmpeg = "bin\\ffmpeg.exe"

mp3in = sys.argv[1]

print "Converting:" , mp3in +".mp3"
os.system("del *.wav")
#Convert to wav
os.system(ffmpeg+" -i " + mp3in +".mp3  m.wav")

#Split Channels
os.system(sox+" m.wav m.1.wav remix 1")
os.system(sox+" m.wav m.2.wav remix 2")

#Split in small tiles
os.system(sox+" m.1.wav pm.1.wav trim 0 3 : newfile : restart")
os.system(sox+" m.2.wav pm.2.wav trim 0 3 : newfile : restart")

#remove unused
os.system("del m.*.wav")

files = os.listdir(".")
leftch = []
rightch = []
for f in files:
    if re.search (  "pm\\.1[0-9]+\\.wav", f):
        leftch.append( f )	
    if re.search (  "pm\\.2[0-9]+\\.wav", f):
        rightch.append( f )			
		
#Randomly apply filters to both channels
for f in leftch:    
    if random.random() > 0.66:
        fmin = 1 #random.randint(1, 2)	
        fmax = 8 #random.randint(3, 5)	
        os.system(sox+" {0} f{0} sinc -a 60 {1}k-{2}k".format( f, fmax, fmin ))
    else:
        os.system(sox+" " + f + " f" + f )

for f in rightch:    
    if random.random() > 0.66:
        fmin = 1 # random.randint(1, 2)	
        fmax = 8 # random.randint(3, 5)	
        os.system(sox+" {0} f{0} sinc {1}k-{2}k".format( f, fmax, fmin ))
    else:
        os.system(sox+" " + f + " f" + f )
		
#Join tiles of each channel
os.system(sox+" fpm.1* c1.wav" )		
os.system(sox+" fpm.2* c2.wav" )		

#Join channels
os.system(sox+" -M c1.wav c2.wav out.wav")
os.system(ffmpeg+" -y -i out.wav " + mp3in + "_tomatis.mp3")
os.system("del *.wav")
