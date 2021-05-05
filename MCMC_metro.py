
import numpy, random, datetime



def metropolis(x_old, a):
    random.seed(datetime.datetime.now())
    
    delta = numpy.random.uniform(-1, 1) 
    
    x_update = x_old + a*delta
    
    R = numpy.exp(-0.5*(x_update**2 - x_old**2))
    
    if R >= 1:
        x_old = x_update 
        print("R>=1")
        return 1 # accept
    elif 0 < R < 1:
        print("0<R<1")
        x_old = x_update
        return 1
    else:
        return 0 # reject

accept = 0
N = 10
x_start = 0
a = 3

for i in range(N):
    accept += metropolis(x_start, a)
    
    print("\n\n\n\nN=", i)
    
accept/=N

print(accept)