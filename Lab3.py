import random 

def studentList():
    
    list = []
    for i in range(10):
        id = random.randint(1,10**9)
        list.append(id)
    return list
def randomGroup(list):
    groupList = []
    i = 0 
    while(i < len(list)):
        
        groupList.append([list[i],list[i+1]])
        i = 2+i
    return groupList


list = studentList()
print(list)
print(randomGroup(list))
