class Student:
    
    def __init__(self,id,name,major):
        self._id=id
        self._name=name
        self._major=major

s1=Student('STUST001','大B','資工')
print("學生s1姓名=",s1._name)
print("學生s1學號=",s1._id)
print("學生s1科系=",s1._major)

s2=Student('STUST002','小A','資工')
print("學生s1姓名=",s2._name)
print("學生s1學號=",s2._id)
print("學生s1科系=",s2._major)


class Course:
    def __init__(self,classcode,classname,學分數,必修選修,teacher,classtime):
        self._classname=classname
        self._teacher=teacher
        self._必修選修=必修選修
        self._學分數=學分數
        self._classtime=classtime
        self._classcode=classcode

c1=Course('20231222','套裝軟體應用','3','選修','李宗儒','Fri 1,2,3')
print("classname=",c1._classname)
print("teacher=",c1._teacher)
print("必修選修=",c1._必修選修)
print("學分數=",c1._學分數)
print("classtime=",c1._classtime)
print("classcode=",c1._classcode)

c2=Course('G0D17V01','深度學習與電腦視覺','3','選修','李宗儒','Tues 2,3,4')
print("classname=",c2._classname)
print("teacher=",c2._teacher)
print("必修選修=",c2._必修選修)
print("學分數=",c2._學分數)
print("classtime=",c2._classtime)
print("classcode=",c2._classcode)