# a bitmath module that setbit,getbit,clearBit,toggleBit
def toggleBit(x,n):
	return (x ^( 1<<n))

def setBit(x,n):
	return (x | (1<<n))

def clearBit(x,n ):
	return (x & ~(1<<n)) 
	
def getBit(x,n) :
	return((x>>n)&1)