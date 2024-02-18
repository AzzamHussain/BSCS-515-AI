# . You have collected information about cities in your province. You decide to store each city’s
# name, population, and mayor in a file. Write a python program to accept the data for a number 
# of
# cities from the keyboard and store the data in a file in the order in which they’re entered.
f=open("newfile.txt","w")
no_Of_cities = int(input("Enter the number of cities: "))

for _ in range(no_Of_cities):
    city_name = input("Enter city name: ")
    population = input("Enter population: ")
    mayor = input("Enter mayor's name: ")
    f.write(f"{city_name}, {population}, {mayor}\n")

print("City data has been saved to newfile.txt file.")
# Open the file in read mode
with open("newfile.txt", "r") as file:
    # Read and print the contents of the file
    print(file.read())

