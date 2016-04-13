#encoding:utf8
#7_1处理异常

#numFailures=0会报错
successFailusrRatio=numSuccesses/float(numFailures)
print 'The success/failure ratio is',successFailusrRatio
print 'Now here'

#跳过异常
try:
    successFailusrRatio=numSuccesses/float(numFailures)
    print 'The sucess/failure ratio is',successFailusrRatio
except ZeroDivisionError:
    print 'No failures so the sucess/failure ratio is undefined.'
print 'Now here'

#若输入'abc'，报错
val=int(raw_input('Enter an integer:'))
print 'THe square of the number you entered is',val**2

#跳过异常
while True:
    val=raw_input('Enter an integer:')
    try:
        val=int(val)
        print 'The square of the number you entered is ',val**2
        break
    except ValueError:
        print val,'is not an integer'

#
def readInt():
    while True:
        val=raw_input('Enter an integer:')
        try:
            val=int(val)
            return val
        except ValueError:
            print val,'is not an integer'

def readVal(valType,requesMsg,errorMsg):
    while True:
        val=raw_input(requesMsg+' ')
        try:
            val=valType(val)
            return val
        except ValueError:
            print val,errorMsg

val=readVal(int,'Enter an integer:','is not an integer')

def getRatios(vect1,vect2):
    '''假定vect1和vect2是列表，长度相同
       返回一个列表，其中的每个元素是vect1[i]/vect2[i]'''
    ratios=[]
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index])/float(vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError ('getRatios called with bad arguments')
        return ratios

# v1=[1,2,3]
# v2=[]
# print getRatios(v1,v2)
#测试
# try:
#     print getRatios([1.0,2.0,7.0,6.0],[1.0,2.0,0.0,3.0])
#     print getRatios([],[])
#     print getRatios([1.0,2.0],[3.0])
# except ValueError,msg:
#     print msg


def getRatios(vect1,vect2):
    '''假定vect1和vect2是列表，长度相同
       返回一个列表，其中的每个元素是vect1[i]/vect2[i]'''
    ratios=[]
    if len(vect1)!=len(vect2):
        raise ValueError('getRatios called with bad arguments')
    for index in range(len(vect1)):
        vect1Elem=vect1[index]
        vect2Elem=vect2[index]
        if (type(vect1Elem) not in (int,float)) or (type(vect2Elem) not in (int,float)):
            raise ValueError('getRatios called with bad arguments')
        if vect2Elem==0.0:
            ratios.append(float('NaN'))  #NaN=Not a Number
        else:
            ratios.append(vect1Elem/vect2Elem)
    return ratios


def getGrades(fname):
    try:
        gradesFile=open(fname,'r')
    except IOError:
        raise ValueError('getGrades could not open' +fname)
    grades=[]
    for line in gradesFile:
        try:
            grades.append(float(line))
        except:
            raise ValueError('Unable to convert line to float')
    return grades
