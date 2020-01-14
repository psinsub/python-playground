#read name.txt into a vairable called my name
with open('name.txt', 'r') as f:
    my_name = f.read()

print(my_name)

#writes a new file named hello.txt with the contents
with open('hello.txt', 'w') as f:
    f.write('hello, this is ' + my_name)
    f.write('\n')

