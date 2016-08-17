class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print '%s:%s' %(self.name,self.score)

    def get_grade(self):
        if self.score>=90:
            print 'A'
        elif self.score>=60:
            print 'B'
        else:
            print 'C'

bart=Student('Bart Simpson',59)
lisa=Student('Lisa Simpson',87)
bart.get_grade()
lisa.get_grade()
bart.score=98
bart.get_grade()
