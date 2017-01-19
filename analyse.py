import sys
import numpy
import matplotlib.pyplot


def detect_problems (filename):
    """some of our temperature files haave problems, check for these

    this function reads a file and reports on odd looking maxima and minimia that add to zero
    the function does not return any data
    """
    data=numpy.loadtxt(fname=filename, delimiter=',')
    
    if numpy.max (data, axis=0)[0] ==0 and numpy.max (data, axis=0)[20] ==20:
        print ('suspicious looking maxima')
    elif numpy.sum(numpy.min(data, axis=0)) ==0:
        print ('minimum adds to zero')
    else:
        print ('data looks ok')
        
def analyse (filename, outfile=None):
    data=numpy.loadtxt(fname=filename,delimiter=',')
    
    """ this function analyses a dataset and outputs plots for maax min and ave
    """
    
    fig=matplotlib.pyplot.figure (figsize=(10.0,3.0))
    subplot1=fig.add_subplot (1,3,1)
    subplot2=fig.add_subplot (1,3,2)
    subplot3=fig.add_subplot (1,3,3)

    subplot1.set_ylabel('average')
    subplot1.plot(numpy.mean(data, axis=0))

    subplot2.set_ylabel('minimum')
    subplot2.plot(numpy.min(data, axis=0))

    subplot3.set_ylabel('maximum')
    subplot3.plot(numpy.max(data, axis=0))
    
    fig.tight_layout()
    if outfile is None:
    matplotlib.pyplot.show
    
    else:
        matplotlib.pyplot.savefig(outfile)
        
print("running",sys.argv[0])
    

print (sys.argv[1])
analyse (sys.argv[1], outfile=sys.argv[2])
detect_problems (sys.argv[1])
    
    