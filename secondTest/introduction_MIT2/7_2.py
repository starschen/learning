#encoding:utf8
# def getRatios(vect1,vect2):
#     ratios=[]
#     for index in range(len(vect1)):
#         try:
#             ratios.append(vect1[index]/float(vect2[index]))
#         except ZeroDivisionError:
#             ratios.append(float('nan'))
#         except:
#             raise ValueError('getRatios called with bad arguments')
#     return ratios
#
# # msg='getRatios called with bad arguments'
# # try:
# #     print getRatios([1.0,2.0,7.0,6.0],[1.0,2.0,0.0,3.0])
# #     print getRatios([],[])
# #     print getRatios([1.0,2.0],[3.0])
# # except ValueError,msg:
# #     print msg
#
# def getRatios(vect1,vect2):
#     ratios=[]
#     msg='getRatios called with bad arguments'
#     if len(vect1)!=len(vect2):
#         raise ValueError,msg
#     for index in range(len(vect1)):
#         vect1Elem=vect1[index]
#         vect2Elem=vect2[index]
#         if type(vect1Elem) not in (int,float) or type(vect2Elem) not in (int,float):
#             raise ValueError,msg
#         if vect2Elem==0.0:
#             ratios.append(float('NaN'))
#         else:
#             ratios.append(vect1Elem/float(vect2Elem))
#     return ratios


#动手练习：实现一个满足下面需求的函数：
def findAnEven(l):
    '''假设l是一个整数列表
       返回l中第一个偶数
       如果l中不包含偶数，触发ValueError异常'''
    s=[]
    for index in range(len(l)):
        if l[index]%2==0:
            s.append(l[index])
    if len(s)==0:
        raise ValueError,'there are not even numbers in the list'
    else:
        return s[0]
# l=[1,3,5,7]
l=[1,2,3,4,5]
print findAnEven(l)

def getGrade(fname):
    try:
        gradesFile=open(fname,'r')
    except IOError:
        raise ValueError('getGrades could not open'+fname)
    grades=[]
    for line in gradesFile:
        try:
            grades.append(float(line))
        except:
            raise ValueError('Unable to convert line to float')
    return grades

try:
    grades=getGrade('quiz1grades.txt')
    grades.sort()
    median=grades(len(grades)//2)
    print 'Median grade is',median
except ValueError,errorMsg:
    print 'Whoops.',errorMsg
