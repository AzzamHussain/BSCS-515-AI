#(i)Write a list comprehension which, from a list, generates a lowercased version of each string that has 
#length greater than five.

list=['Azzam','yaseen','Huzaifa','laraib','Mustafa']
#newList=[]
new_list = [element.lower() for element in list if len(element) > 5]

# for elements in list:
#     if elements.islower():
#         newList.append(elements)

print(new_list)