# >> here message is actually what we call a variable, and the one which is written in single quotes is called string (a group of characters).
# message = 'Hello World'

# >> this is how we execute our code in python.
# print(message)

# >> finding the length of a string.
#print(lenth.message) # This is wrong, will get an error in terminal.
# print(len(message)) #correct code.

# >> to locate any alphabet in a string.
#print(message[1:6]) # it includes all the characters between the beginning and upto but not including the 6th index.
# >> this thing is called slicing >> https://www.youtube.com/watch?v=ajrtAuDg3yw

# Some methods of strings (function) you can call to perform operations, for example;

# 1. if we want to get our characters in lowercase.
# print(message.lower())

# 2. if we want to get our characters in uppercase.
# print(message.upper())

# 3. in case we want to see how many time any particular character occured in a string.
# print(message.count('World')) # we must have to pass an argument in order to find what we're looking for.

# 4. if we want to see what character lies on any certain index.
# print(message.find('World')) # so, we got to know that 'World' lies on 6th index by passing it as an argument in the print statement. But, if you pass a character which doesn't even exist in your string, you'll get -1 in terminal.
# print(message.find('w'))

# 5. if i want to replace a character.
# i must have to pass 2 arguments for that, the first one must be the one that already exist, the second one to which i want it to be replaced.
# print(message.replace('World', 'Universe')) # 1 method of doing this
# message = message.replace('World', 'Universe') # 2 method of doing this
# print(message) 

# 6. add multiple strings and concatenate them altogether.
greeting = 'Hello'
name = 'Maddy'

# >> one way of creating spacing between strings during concatenation.
# message = greeting + ', ' + name 
# >> another method is to add curly brackets instead of variables and can even modify the variable too, at last just add .format (variable, variable).
# message = '{}, {}. Welcome!' .format(greeting, name) 

# print(message) 
# #string formatting >> https://www.youtube.com/watch?v=vTX3IwquFkc&t=0s

# 7. Using f string method for string formatting.
message = f'{greeting}, {name}. Welcome!'
# >> using f string method we simply put variables inside the curly braces, even can use different functions on variables using f string method.
message = f'{greeting.replace('Hello', 'Salam')}, {name.upper()}. Welcome!'
print(message)