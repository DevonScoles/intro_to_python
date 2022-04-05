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


my_message = 'Brad\'s World' #use backslashes before single quotes inside of single quotes
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
combined_message = message + "," + new_message
print(combined_message)
# print(f'{message} , {new_message} and goodnight!')
print("{}, {} And goodnight!".format(message, new_message), '\n')

print("="*15,'Taking user input',"="*15)
user_name = str(input("What's your name? "))
print(user_name)
user_sirname = str(input("What's your last name? "))
full_name = user_name + ' ' + user_sirname
print(full_name)