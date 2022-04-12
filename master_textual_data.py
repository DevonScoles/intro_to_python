print('<'*25,"Begining",'>'*25)
print('Hello World \n') #textual data or Strings can go in 'singular' or "double" quotes
# This is a print statement. Anything can go inside of the parantheses that you want to output
# the print statement is the most essential tool you'll need for python
# it's not just for outputing words when you run the program it's literally for outputting anything you need to look at
# If you have a function, variable, algorithm, string, etc and you need to know the value of it
# you can literally just print it unless you have an error 
# Backslash n inside of quotes is like hitting enter in a google or word doc

print("="*15,'Printing using String Variables',"="*15)
message = 'Hello World' #this is a string Variable called message
# Everything in computer science is case sensitive... message != Message
print(message)
print(message, ", however this will print everything on the same line.")
# use commas to print more than one item in a print statement


my_message = 'Devon\'s World' #use backslashes before single quotes inside of single quotes
print('How many characters are in my_message: using len(variable_name)')
print(len(my_message),'\n') # print len() function to get the amount of characters in a String


print("="*15,'Individual Character printing','='*15)
print(message[0])
print(message[1:8])
print(message[-1])
print('How many Ls are in message?', message.count('l'),'\n')
# to print a specific character of the string use [] at the end of the variable name

print("="*15,'Replacing Characters or Words within an existing String',"="*15)
#Rather than going back to edit a String you can use the .replace('parameter 1', 'parameter 2') function like this...
new_message = message.replace('Hello', 'Goodbye')
message = message.replace('Hello', 'Good Evening')
print('This is our new message:', new_message)
print('This is our redefined message variable:',message,'\n')

print("="*15,'Manipulating String data Cont. (adding strings together)',"="*15)
combined_message = message + ', ' + new_message
print(combined_message)
print(f'{message}, {new_message} and goodnight!')
print('{}, {} And Goodnight!'.format(message, new_message),'\n')


print("="*15,'Taking user input',"="*15)
user_name = input('What is your name? ') 
#the above line will prompt the user asking their name and assign whatever they type after the prompt to the variable user_name
user_sirname = input()
#above line will take user input without displaying any prompt
print(user_name, user_sirname)

print("="*15,'How is this important/useful???','='*15)
# Below is a function I prepared for a tech interview for a company I'll be working for this summer
# in New York City and New Haven Connecticut.

def madLib(): #this is a function called MadLib that takes no parameters inside the parantheses

    #print statement to say Madlib time!!! and then go down two lines
    print("MadLib time!!!\n")

    #these are variables that take ask you for words
    pluralNoun = input("Give me a plural noun: ")
    adjective = input("Now an adjective: ")
    pluralAnimal = input("How about an animal: ")
    adjAnimal = input("Now I need an adjective and animal: ")
    animal2 = input("Another animal: ")
    adjective2 = input("Okay now I need another adjective: ")
    pluralAnimal = input("Now I need a plural animal: ")
    adjective3 = input("Give me another adjective: ")
    food = input('Whats a funky food?: ')
    drink = input('Apple juice or gatorade?: ')
    adjective4 = input("Give me another adjective: ")
    pluralAnimal2 = input("Plural animal: ")
    housing = input("A fun palce to live: ")
    pluralAnimal3 = input("last but not least another plural animal: ")


    #this is the print statement inside of the function you can tell because it looks indented
    print(f'\nSo many {pluralNoun} make {adjective} pets. \nMany people like furry {pluralAnimal} or a {adjAnimal} to cuddle with. \
    \nSome people like having a {animal2} for a pet, and others prefer {adjective2} {pluralAnimal}. \nMost pets need things like {adjective3} \
    care, {food}, {drink}, exercise, and a {adjective4} place to sleep. \nSome pets like {pluralAnimal2} live in {housing},\
    but everyone can agree that {pluralAnimal3} are cute and crazy') 

madLib()
