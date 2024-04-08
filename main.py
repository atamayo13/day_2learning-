# #order of execution
# # in python

# print("hello world")
# #strings are surronded by quotes 
# #single or double quotes '' or ""
# #be consistent with the quotes you use
# print("order of execution")
# print("in python")
# print("*"*20)

# #variable are used to store data
# #variable are created when you assign a value to it
# #variables are case sensitive
# price= 10 #integer variable
# name= "John" #string
# rating= 4.9 #float variable
# is_published= True #boolean variable
# #start all variable with a lower case letter or underscore
# #use camel case if you want to start with a capital letter
# #on the next word
# playerBulls = "michael jordan"

# #Concatentation to join variables in a sentence
# print(name + "is a basketball player")
# print(name + "has a rating of " + str(rating))
# #use the str() function to convert a number to a string
# #the pluss sign is used to concatentation strings
# print("the price of the book is " + str(price)) 

# # #getting input from the use
# name= input("what is your name?")
# age = input("what is your age")
# print("hello " + name + "you are" + age + "years")

#ask two questions from the user
#persons name and favorite color
#then print a message like "Moses likes blue"

personName=input("what is your name?")
favoriteColor = input ("what is your fav color?")
print(personName + "likes" + favoriteColor)