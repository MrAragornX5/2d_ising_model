import numpy, time, random

def PDF_gauss(x):
    return 0.5*numpy.sqrt(numpy.pi)*numpy.exp(-0.5*numpy.power(x, 2))


def metropolis(x_start, a, N):
    
    random.seed(time.time())
    markov_chain = numpy.zeros(N)
    
    accept, reject = [], []
    
    x_old = x_start
    markov_chain[0] = x_old
    
    for i in range(0, N):
        delta = numpy.random.uniform(-1, 1)
        x_new = x_old + a*delta
        
        R = PDF_gauss(x_new)/PDF_gauss(x_old)
        
        if R >= 1:
            markov_chain[i] = x_new
            accept.append(x_new)
        else:
            x_ran = numpy.random.uniform(0, 1)
            if x_ran < R:
                markov_chain[i] = x_new
                accept.append(x_new)   
            else:
                x_old = markov_chain[i-1]
                markov_chain[i] = x_old
                reject.append(x_old)
    
    #accept_rate = len(accept)/N
    return markov_chain
