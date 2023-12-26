my_string = 'The string'
rev_string = ''
length = len(my_string)

for i in range(length-1, -1, -1):
    rev_string += my_string[i]

print(rev_string)
