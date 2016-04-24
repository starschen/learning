#encoding:utf8
#15.1弹簧的行为

import pylab
#从文件中提取数据
def getData(fileName):
    dataFile=open(fileName,'r')
    distances=[]
    masses=[]
    discardHeader=dataFile.readline()
    for line in dataFile:
        d,m=line.split(' ')
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close
    return (masses,distances)

#绘制数据
def plotData(inputFile):
    masses,distances=getData(inputFile)
    masses=pylab.array(distances)
    distances=pylab.array(distances)
    forces=masses*9.81
    pylab.plot(forces,distances,'bo',label='Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance(meters)')

# plotData('springData.txt')
# pylab.show()
#使用曲线拟合数据
def fitData(inputFile):
    masses,distances=getData(inputFile)
    masses=pylab.array(distances)
    distances=pylab.array(distances)
    forces=masses*9.81
    pylab.plot(forces,distances,'bo',label='Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance(meters)')
    #find linear fit
    # a,b=pylab.polyfit(forces,distances,1)
    # predictedDistances=a*pylab.array(forces)+b
    # k=1.0/a
    # pylab.plot(forces,predictedDistances,label='Displacements predicted by\nlinear fit,k='+str(round(k,5)))
    # pylab.legend(loc='best')
    #find 3 times fit
    a,b,c,d=pylab.polyfit(forces,distances,3)
    predictedDistances=a*(forces**3)+b*forces**2+c*forces+d
    pylab.plot(forces,predictedDistances,'b:',label='cubic fit')

fitData('springData.txt')
pylab.show()
