import random 

def studentList():
    print("hi")
    list = []
    for i in range(10):
        id = random.randint(1,10**9)
        list.append(id)
    return list
print(studentList())
