import pandas as p

data = {
    "id":[1,2,3],
    "name":["user1","user2","user3"],
    "age":[12,32,45],
    "salary":[30000,45000,60000]
    }

pd =p.DataFrame(data)

print(pd)

