#encoding:utf8
#15.2弹丸的行为
#绘制弹丸的轨道
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
    #生成一个数组，用于存储每个距离的平均高度
    totHeights=pylab.array([0]*len(distances))
    for h in heights:
        totHeights=totHeights+pylab.array(h)
    meanHeights=totHeights/len(heights)
    pylab.title('Trajectory of Projectile (Mean of'+str(numTrials)+'Trials)')
    pylab.xlabel('Inches from Launch Point')
    pylab.ylabel('Inches Above Launch Point')
    pylab.plot(distances,meanHeights,'bo')
    a,b=pylab.polyfit(distances,meanHeights,1)
    altitudes=a*distances+b
    pylab.plot(distances,altitudes,'b',label='Linear Fit')
    a,b,c=pylab.polyfit(distances,meanHeights,2)
    altitudes=a*(distances**2)+b*distances+c
    pylab.plot(distances,altitudes,'b:',label='Quadratic Fit')
    pylab.legend()

    #计算R＊＊2
    def rSquared(measured,predicted):
        '''measured是一个一维数组，包含所有测量值，predicted包含所有预测值，返回决定系数'''
        estimateError=((predicted-measured)**2).sum()
        meanOfMeasured=measured.sum()/float(len(measured))
        variability=((measured-meanOfMeasured)**2).sum()
        return 1-estimateError/variability

    print 'RSquare of linear fit=',rSquared(meanHeights,altitudes)

    #计算弹丸的速度
    def getHorizontalSpeed(a,b,c,minX,maxX):
        '''minX和maxX是距离，单位是英尺
           返回水平速度，单位是英尺／秒'''
        inchesPerFoot=12.0
        xMid=(maxX-minX)/2.0
        yPeak=a*xMid**2+b*xMid+c
        g=32.16*inchesPerFoot #accel. of gravity in inches/sec/sec
        t=(2*yPeak/g)**0.5
        print 'Horizontalspeed=',int(xMid/(t*inchesPerFoot)),'feet/sec'
    getHorizontalSpeed(a,b,c,distances[-1],distances[0])
processTrajectories('tanwan.txt')

# pylab.show()
