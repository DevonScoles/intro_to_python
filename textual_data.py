print('<'*25,"Begining",'>'*25) # use '\n' to create a new line inside of a string
print("hello world\n")

print("="*15,'Printing using String Variables',"="*15)
message = 'Hello World' #message != Message
print(message)
print(message, message, "this print statement is printing 3 things\n")

print("="*15,'Individual Character printing','='*15)
print(message[0])
print(message[0:7]) #python uses : instead of a dash to say 0 through 7 
print(message[-1])
print(len(message)) #len(message) # len means the length of the word, it counts all the characters in the string
print(message.count('l')) #.count() #.count() will count how many ls there are any letter when you put in paranthesis

print("="*15,'Replacing Characters or Words within an existing String',"="*15)
new_message = message.replace('Hello','Goodbye') #replace() will replace the old world with a new one
print(new_message)
message = message.replace('World','earth')
print(message)

print("="*15,'Manipulating String data Cont. (adding strings together)',"="*15)





print("="*15,'How is this important/useful???','='*15)