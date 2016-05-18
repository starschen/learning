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

# clear(1000,0.01,1000)
# pylab.show()

def successfulStarts(eventProb,numTrials):
    triesBeforeSuccess=[]
    for t in range(numTrials):
        consecFailures=0
        while random.random()>eventProb:
            consecFailures+=1
        triesBeforeSuccess.append(consecFailures)
    return triesBeforeSuccess

random.seed(0)
probOfSuccess=0.5
numTrials=5000
distrbution=successfulStarts(probOfSuccess,numTrials)
pylab.hist(distrbution,bins=14)
pylab.xlabel('Tries befor Success')
pylab.ylabel('Number of Occurrences Out of'+str(numTrials))
pylab.title('Probability of Starting Each Try'+str(probOfSuccess))
pylab.savefig('12_3successfulStarts')
pylab.show()
