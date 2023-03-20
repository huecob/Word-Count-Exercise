"""Count words in file."""

import sys

data = open(sys.argv[1])

    #create an empty dictionary
ret_val = {}
    #loop through the text file
    #write a conditional for loop
    #conditions will be if this word does not exist within the empty dictionary
    #set that value to 1
    #else add 1

    #return our dictionary
for line in data:
    line = line.rstrip()
    words_list = line.split(" ")
    for word in words_list:
        if word not in ret_val:
            ret_val[word] = 1
        else:
            ret_val[word] += 1
    

for word, count in ret_val.items():
    print(word, count)

