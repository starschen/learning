import pylab
def getData(fileName):
    dataFile=open(fileName,'r')
    distances=[]
    masses=[]
    discardHeader=dataFile.readline()
    for line in dataFile:
        d,m=line.split(' ')
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses,distances)

def plotData(inputFile):
    masses,distances=getData(inputFile)
    masses=pylab.array(masses)
    distances=pylab.array(distances)
    forces=masses*9.81
    pylab.plot(forcer,distances,'bo',label='Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')

def fitData(inputFile):
    masses,distances=getData(inputFile)
    distances=pylab.array(distances)
    masses=pylab.array(masses)
    forces=masses*9.81
    pylab.plot(forces,distances,'bo',label='Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')

    a,b=pylab.polyfit(forces,distances,1)
    predictedDistances=a*pylab.array(forces)+b
    k=1.0/a
    pylab.plot(forces,predictedDistances,label='Displacements predicted by\nlinear fit,k='+str(round(k,5)))
    pylab.legend(loc='best')

    a,b,c,d=pylab.polyfit(forces,distances,3)
    predictedDistances=a*(forces**3)+b*(forces**2)+c*forces+d
    pylab.plot(forces,predictedDistances,'b:',label='cubic fit')
