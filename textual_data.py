from email import message


print('<'*25,"Begining",'>'*25) # use '\n' to create a new line inside of a string
print ("Hello World\n")

print("="*15,'Printing using String Variables',"="*15)
message = "Hello World"
print (message)
print (message, message, " this print statement is print 3 things\n")


print("="*15,'Individual Character printing','='*15)
print (message[0])
print (message[0:7])
print (message[-1])
print (len(message))
print (len("message"))
print (message.count("World"))


print("="*15,'Replacing Characters or Words within an existing String',"="*15)
new_message = message.replace("Hello", 'Goodbye')
print (new_message)
new_message = message.replace("Hello", 'Goodbye')
print (new_message)



print("="*15,'Manipulating String data Cont. (adding strings together)',"="*15)





print("="*15,'How is this important/useful???','='*15)