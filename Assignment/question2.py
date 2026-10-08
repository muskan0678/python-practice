# # 1. Write a function named welcome_message() that prints “Welcome to
# # Python Programming!” three times.

# def welcome_message():
#     print("WElcome to Python Course")

# welcome_message()
# welcome_message()
# welcome_message()

# 2. 2. Define a function inspire() that prints a motivational quote with your
# name.

# FUNCTION DEFINATION , we have only defined the function here 
# def inspire():
#     print("You are the master of your destiny: Muskan Parween")

# inspire()

#3. Create a function good_morning() that prints "Good Morning, Saumya!".
# Call it twice.

# def twice():
#     print("Good Morning, Mussu!")

# twice()

# 4. Why are functions used in programming? Write two advantages.

# Q1. write a program to read a text from a given file certificate.tst and find whether it contains the word live.
file= open("CHAPTER 8/certificate.txt", "r")
dataOfFile= file.read()

dataOfFile= dataOfFile.lower()

if "live" in dataOfFile:
    print("Yes Live word is present in the file")
else:
    print("No")

# Q2. open a file called report.txt in write mode.

file= open("report.txt", "w")
file.write("Kafi sahi se py. sikh rhe h mja aa rha he bhaut")