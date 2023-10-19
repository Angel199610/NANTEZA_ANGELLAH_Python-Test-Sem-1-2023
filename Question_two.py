#Function to find th eaverage of two numbers 
def average_two (x, y):
    x = 0
    y = 5
    average = (x + y)/2
    return average


#Test the program with 2 different numbers 
x = 5
y = 20
result = average_two(x, y)
print(f"The Average of x and Y is:",{result})


#A program that asks the user to input 3 numbers and find minimum number
list_1 = float (input("Enter Your first number: "))
list_2 = float (input("Enter Your Second number: "))
list_3 = float (input("Enter Your third number: "))
minimum_number = min(list_1, list_2, list_3)
print(f"The Minimum number of the test is: ", {minimum_number})