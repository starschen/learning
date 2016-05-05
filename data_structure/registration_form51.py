#encoding:utf8
#page 51:建立一个教师和学生基本情况的登记表

studentsLabel=['num','name','sex','age','job','whichClass']
teachersLabel=['num','name','sex','age','job','title']
student={}.fromkeys(studentsLabel)
teacher={}.fromkeys(teachersLabel)
for i in studentsLabel:
    print i,':'
    student[i]=raw_input()
for key,val in student.items():
    print key,':',val
