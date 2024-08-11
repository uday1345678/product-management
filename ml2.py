""" import pandas

studentinfo=[
            {"name":"uday","age":14,"class1":9},
            {"name":"uday2","age":15,"class1":10}
            ]

p1=pandas.DataFrame(studentinfo)
print(p1)
print(p1['name'])
print(p1['age'])
print(p1['class1'])

 """
""" 
import pandas as pd

studentinfo=[
            {"name":"uday","age":14,"class1":9},
            {"name":"uday2","age":15,"class1":10}
            ]

p1=pd.DataFrame(studentinfo)
print(p1)
print(p1['name'])
print(p1['age'])
print(p1['class1']) """
""" 
import pandas as pd

name=["user1","user2","user3"]
age=[19,20,23]

p1=pd.Series([name,age],index=["name","age"])
print(p1) """
""" 
import pandas as pd

name=["user1","user2","user3"]
age=[19,20,23]
 """
""" f =pd.DataFrame([name,age])
print(f)


f1 =pd.DataFrame([name,age],index=["name","age"])

print(f1)
 """
""" f1 =pd.DataFrame([name,age],index=["name","age"],columns=["N1","N2","N3"])

print(f1)
 """

import numpy as np
num =[1,2,3,4,5]
""" 
f = np.sin(num)
print(f)
f = np.cos(num)
print(f)
f = np.tan(num)
print(f) """
f =np.sum(num)
print(f)




