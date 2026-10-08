# 1. program that takes a sentence and prints
# total character(len())
# Uppercase version
# Lowercase version

# sentence= input("Enter a sentence: ")

# print("Total character:", len(sentence))
# print("Uppercase:", sentence.upper())
# print("Lowercase:", sentence.lower())



# 2. py program that takes any word or sentence as input and prints
# first character
# last character
# total number of characters

# word= input("Enter a word or sentence: ")

# print("First character:", word[0])
# print("Last character:", word[-1])
# print("Total characters:", len(word))

# c-4 practice question
# 1.take input and print positive if num is greater than zero and so

# num= int(input("Enter a number :"))

# if(num>0):
#     print("Positive")
# elif(num==0):
#     print("Zero")
# else:
#     print("Negative")

# 2. take 3 food and store in list, print and length

# food1= input("Enter food 1:")
# food2= input("Enter food 2:")
# food3= input("Enter food 3:")

# foodList= []
# foodList.append(food1)
# foodList.append(food2)
# foodList.append(food3)

# foodList= [food1, food2, food3]

# print(foodList)
# print(len(foodList))

# c-5
# Create a dictionary named marks to store marks of 3 subjects.
# Add the subjects one by one and print the final dictionary.

# marks= {}
# print(type(marks))

# marks["Math"]= 99
# marks["Science"]= 91
# marks["Chemistry"]= 89

# print(marks)

# 2. You are given a list of programming languages:
# ["Python", "Java", "C++", "Python", "Java", "C"]
# Convert it into a set and print how many unique languages Divya knows.

# programmingList= {"Java", "C++", "Py", "Java", "C"}
# print(type(programmingList))
# print(programmingList)

# # how to convert a list into set

# programmingSet= set(programmingList)
# print(type(programmingSet))
# print("Mussu knows these many language", len(programmingSet))

# 3..create a dictionary storing meaning of 3 english word

# meanings= {
#     "Happy": "Feelings control ",
#     "Brave": "Always truth",
#     "Honestly": "honest everyone",
# }

# print(meanings)

# 4.Create a set of numbers and show union and intersection with another set.

# set1= {1, 2, 3, 4, 5}
# set2= {6, 7, 8, 9, 10}

# Union= set1.union(set2)
# intersection= set1.intersection(set2)

# print("Union:", Union)
# print("Intersection:", intersection)

# 5. Try to add both integer 9 and float 9.0 to a set and observe what happens.

# myset= {9, 9, 0}

# print(myset)
# print(len(myset))

# 6py - 1. write a py program to print numbers from 1 to 10 using  a while loop/

# i= 1

# while(i<=10):
#     print(i)
#     i+=1

# Write a program to print numbers from 10 down to 1 using a while loop.
# (Hint: start from 10 and decrease the counter each time.)

# even num = 2, 4, 6, 8

# num= 1

# while (num<=50):
#     if(num%2 == 0):
#         print(num)
#     num= num+1

# Q. Write a program that prints the sum of first n natural numbers.
# For example, if n = 5, then output should be 1 + 2 + 3 + 4 + 5 = 15.
# (Hint: Keep a running total inside the loop.)

# n= int(input("Enter a number: "))
# sum= 0

# while n>=1:
#     sum= sum+n
#     n= n-1

#     print("Sum= ", sum)
#     print("n= ")

# 5. Write a program to print this pattern using a while loop:
# *
# * *
# * * *
# * * * *

# n= 1

# while n<=4:
    # print("*" * n)
    # n= n+1

    # print("We are out of the while loop, and value of n should be 5. is it 5? check :", n )

# Saumya wants to print her name 5 times, but each time with a number in
# front of it. Write a program using a while loop that prints:

# n= int(input("Enter a number : "))
# i= 1


# while i<=10:
#     print(f"{n} x {i} = {n*i} ")
#     i= i+1
#Q.  Write a program using for and range() to print all even numbers between 1
# and 20.

# for i in range(2, 21, 2):
#     print(i)

# Q. Why are functions used in programming? Write two advantages.

# def square(num=10):
#     return num**2

# print(square(3))

# Write a function that takes a string and returns the count of vowels and
# consonants separately.

def countVowConso(userInput):

    #define vowels
    vowels= "aeiouAEIOU"

    countVowel= 0
    countConsonants= 0

    #SAUMYA123
    for eachChar in userInput:
        if(eachChar.isalpha()):
            if(eachChar in vowels):
                countVowel= countVowel+1
            else:
                countConsonants+=1

    return countVowel, countConsonants


# Function Call

vowels, consonants= countVowConso("Saumya Singh")

print(vowels, consonants)
# print(vowel)