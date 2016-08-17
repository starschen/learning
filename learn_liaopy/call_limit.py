class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError('bad score')


    def print_score(self):
        print '%s:%s' %(self.__name,self.__score)

    def get_grade(self):
        if self.__score>=90:
            print 'A'
        elif self.__score>=60:
            print 'B'
        else:
            print 'C'

bart=Student('Bart Simpson',59)
lisa=Student('Lisa Simpson',87)
# bart.get_grade()
# lisa.get_grade()
# bart.score=98
# bart.print_score()
# print bart.get_name()
# bart.set_score(71)
# print bart.get_score()
print bart._Student__name
