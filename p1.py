""" class studentmanagement:
    def studentmngmnt(self):
        while(True):
            print("studentmngmnt")
            n2=int(input("enter 1 for teacher/nenter2 for student/n enter 3 for studentmngmnt"))
            if (n2==1):
                t=teacher
                t.teacher()
            elif(n2==2):    
                s=student
                s.student()
        
        
object=studentmanagement()
object.studentmngmnt()
 """

class student:
    def __init__(self):
        print("hello")
object=student()


