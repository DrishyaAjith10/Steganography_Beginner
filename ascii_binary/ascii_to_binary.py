message = "hi"

for char in message:
    print(ord(char))

binary_list = []

for char in message:
    binary_list.append(format(ord(char),'08b'))

for i in binary_list:
    print(chr(int(i,2)))