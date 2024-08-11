import pandas as p 
studentname={
    "student1":["user1","user2","user3"],
    "studentmarks":[56,67,76],
    "result":["fail","pass","pass"]

    }
f=p.DataFrame(studentname)
print(f)
print(f["studentmarks"][0])
s=sum(f["studentmarks"])
print(s)
s1=min(f["studentmarks"])
print(s1)

