list=['Azzam','yaseen','Huzaifa','laraib','Mustafa']
newList=[]
for elements in list:
    if elements.islower():
        newList.append(elements)

print(newList)