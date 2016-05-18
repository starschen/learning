import pylab
def getTrajectoryData(fileName):
    dataFile=open(fileName,'r')
    distances=[]
    heights1,heights2,heights3,heights4=[],[],[],[]
    discardHeader=dataFile.readline()
    for line in dataFile:
        d,h1,h2,h3,h4=line.split(' ')
        distances.append(float(d))
        heights1.append(float(h1))
        heights2.append(float(h2))
        heights3.append(float(h3))
        heights4.append(float(h4))
    dataFile.close()
    return (distances,[heights1,heights2,heights3,heights4])

def processTrajectories(fileName):
    distances,heights=getTrajectoryData(fileName)
    numTrials=len(heights)
    distances=pylab.array(distances)
    totHeights=pylab.array([0]*len(distances))
    for h in heights:
        totHeights=totHeights+pylab.array(h)
    meanHeights=totHeights/len(heights)
    pylab.title('Trajectory of Projectile (Mean of '+str(numTrials)+' Trials)')
    pylab.xlabel('Inches from Launch Point')
    pylab.ylabel('Inches Above Launch Point')
    pylab.plot(distances,meanHeights,'bo')
    a,b=pylab.polyfit(distances,meanHeights,1)
    altitudes=a*distances+b
    pylab.plot(distances,altitudes,'b',label='Linear Fit')
    print 'RSquare of linear fit=',rSquared(meanHeights,altitudes)
    a,b,c=pylab.polyfit(distances,meanHeights,2)
    altitudes=a*(distances**2)+b*distances+c
    pylab.plot(distances,altitudes,'b:',label='Quadratic Fit')
    print 'RSquare of Quadratic fit=',rSquared(meanHeights,altitudes)
    pylab.legend()
    pylab.savefig('15_2trajectory')
    getHorizontalSpeed(a,b,c,distances[-1],distances[0])


def rSquared(measured,predicted):
    estimateError=((measured-predicted)**2).sum()
    meanOfMeasured=measured.sum()/float(len(measured))
    variability=((measured-meanOfMeasured)**2).sum()
    return 1-estimateError/variability


# pylab.show()

def getHorizontalSpeed(a,b,c,minX,maxX):
    inchesPerFoot=12.0
    xMid=(maxX-minX)/2
    yPeak=a*(xMid**2)+b*xMid+c
    g=32.16*inchesPerFoot
    t=(2*yPeak/g)**0.5
    print 'Horizontalspeed=',int(xMid/(t*inchesPerFoot)),'feet/sec'

processTrajectories('trajectoryData.txt')
