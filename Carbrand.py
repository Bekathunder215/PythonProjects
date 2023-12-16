#this project is for string concatination
#we want to create a string that says, my favorite car is ____
car = input("I am you, what is your favorite car brand??\n -> ")
car1 = input("and what about the model??\n -> ")

print("My favorite car brand is " + car + "and specifically the model " + car1)
print("My favorite car brand is {} and specifically the model {}".format(car, car1))
print(f"My favorite car brand is {car} and specifically the model {car1}")
#this was a programm