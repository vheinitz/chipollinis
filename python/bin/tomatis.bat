SET PATH="C:\Program Files (x86)\sox-14-4-2"
del *.wav
ffmpeg -i %1  m.wav

sox m.wav m.1.wav remix 1
sox m.wav m.2.wav remix 2

sox m.1.wav pm.1.wav trim 0 10 : newfile : restart
sox m.2.wav pm.2.wav trim 0 10 : newfile : restart

sox pm.1001.wav pmf.1001.wav  
sox pm.1002.wav pmf.1002.wav sinc 5k-1k
sox pm.1003.wav pmf.1003.wav 
sox pm.1004.wav pmf.1004.wav sinc 8k-1k 
sox pm.1005.wav pmf.1005.wav 
sox pm.1006.wav pmf.1006.wav sinc 3k-1k
sox pm.1007.wav pmf.1007.wav  
sox pm.1008.wav pmf.1008.wav sinc 8k-1k
sox pm.1009.wav pmf.1009.wav 
sox pm.1010.wav pmf.1010.wav sinc 6k-1k 
sox pm.1011.wav pmf.1011.wav 
sox pm.1012.wav pmf.1012.wav 

sox pm.2001.wav pmf.2001.wav  
sox pm.2002.wav pmf.2002.wav  
sox pm.2003.wav pmf.2003.wav sinc 5k-1k
sox pm.2004.wav pmf.2004.wav  
sox pm.2005.wav pmf.2005.wav sinc 7k-1k
sox pm.2006.wav pmf.2006.wav 
sox pm.2007.wav pmf.2007.wav sinc 8k-1k 
sox pm.2008.wav pmf.2008.wav 
sox pm.2009.wav pmf.2009.wav sinc 3k-1k
sox pm.2010.wav pmf.2010.wav 
sox pm.2011.wav pmf.2011.wav  
sox pm.2012.wav pmf.2012.wav 

sox pmf.10* c1.wav
sox pmf.20* c2.wav

sox -M c1.wav c2.wav out.wav
ffmpeg -y -i out.wav %1_tomatis.mp3
del *.wav
