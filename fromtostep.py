#!//usr/bin/python
#modification of standard python range function
#uses: numpy arange function

from numpy import arange

def fromtostep_fl (f, t, s):
    #f=from; t=to (end of range); s=step
    f1=float(f)
    s1=float(s)
    t1=float(t)
    return arange (f1, t1+s1/2.0, s1)
	
def fromtostep_int (f, t, s):
	#f=from; t=to; s=step
	f1=int(f)
	t1=int(t)
	s1=int(s)
	return arange (f1, t1+s1/2, s1)
