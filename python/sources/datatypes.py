#DATA TYPES

#String
print (type("Hello"[4]))
#first caracter of string, 0 discribe the firste
print ("123" + "345")
#will print the all numbers
#for strings we add " "

#Intger
print (23 + 2)

#Float
3.23

#Boolean
True
False
String, Intger, float, bolean
num_char = len(input("What is my name?"))
print (type(num_char))

# The Type will show what data type it is

#Type convert to String
new_num_char = str(num_char)
print ("your name has " + new_num_char + " chatacters.")
#To allow this print to work we need to convert the varibale num_char from Intger to String

#Data TYPE INTGER
a = 123
print(type(a))
#DATA TYPE CONVERT TO STRING
a = str(123)
print(type(a))

#BREAK THE IMPUT NUMBER TO TWO VARIABLES AND SUM BETWEEN THEM
two_digit_number = input("Type a two digit number: ") # print (type(two_digit_number))
# print (two_digit_number + two_digit_number)
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
print(first_digit)
print (second_digit)
two_digit_number = first_digit + second_digit
print (type(two_digit_number))

#F-String - Allow you to mix diff DataTypes by using "f"
#By using after the print(f) and attchaed the variables with {} as score, will allow us mix between the diffreant data types, (Intger, Float, Boleian)
score = 0
height = 2.3
IsWinning = True
#F-String exemple
print(f"hellow is score is {score},The height is - {height}, we are winning {IsWinning}")