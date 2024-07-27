information=[
            {"id":5,"name":5,"class1":"5th"},
            {"id":6,"name":"pata nahi","class1":"7th"}
]       

class Profile:
    def __init__(self,profile):
        print(profile)
class user:
    def __init__(self):
        print(information)
        self.u=input("enter name")
        self.c=input("enter class")
    def studentadd(self):
    
        information.append({"id":7,"name":self.u,"class1":self.c})
    def printinfo(self):
        print(information)


    def search(self):
        na=input("enter name")
        for i in information:
            if(na==i['name']):
                print("thank you")
                p=Profile(i)
                break
        else:
            print("soryyyyy")
    

user1=user()
user1.studentadd()
user1.printinfo()
user1.search()
