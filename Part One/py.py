file = open('motto.txt', 'w')
file.write('Fiat Lux!\n')
file.close()

file = open('motto.txt', 'r')
content = file.read()
print ("Initial content of the file:")
print (content)
file.close()

file = open('motto.txt', 'a')
content = file.write('Let there be light!\n')
print (content)
file.close()

file = open('motto.txt', 'r')
content = file.read()
print (f"Content of the string after appending: {content}")
file.close()