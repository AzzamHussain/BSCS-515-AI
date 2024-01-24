#(ii)Write a Python program to count the number of strings where the string length is 2 or more and the 
#first and last character are same from a given list of strings. 
String_List = ['abc', 'xyz', 'aba', '1221']
counter = 0

for i in String_List:
    if len(i) >= 2 and i[0] == i[-1]:
        counter += 1

print("Expected Result:", counter)
