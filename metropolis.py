import numpy, time

def PDF_gauss(x):
    return 0.5*numpy.sqrt(numpy.pi)*numpy.exp(-0.5*numpy.power(x, 2))

def metropolis(x_start, a, N):
    
    numpy.random.seed(int(time.time()))
    markov_chain = numpy.zeros(N)
    
    accept, reject = 0, 0
    
    x_old = x_start
    markov_chain[0] = x_old
    
    for i in range(0, N):
        delta = numpy.random.uniform(-1, 1)
        x_new = x_old + a*delta
        
        R = PDF_gauss(x_new)/PDF_gauss(x_old)
        
        if R >= 1:
            markov_chain[i] = x_new
            accept+=1
        else:
            x_ran = numpy.random.uniform(0, 1)
            if x_ran < R:
                markov_chain[i] = x_new
                accept+=1   
            else:
                markov_chain[i] = markov_chain[i-1]
                reject+=1
    
    return markov_chain