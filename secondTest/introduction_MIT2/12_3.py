import random
import pylab
vals=[1,200]
for i in range(1000):
    num1=random.choice(range(1,100))
    num2=random.choice(range(1,100))
    vals.append(num1+num2)
# pylab.hist(vals,bins=10)
# pylab.savefig('12_3hist')
# pylab.show()

def clear(n,p,steps):
    numRemaining=[n]
    for t in range(steps):
        numRemaining.append(n*((1-p)**t))
    pylab.plot(numRemaining)
    pylab.xlabel('Time')
    pylab.ylabel('Molecules Remaining')
    pylab.title('Clearance of Drug')

clear(1000,0.01,1000)
pylab.show()
