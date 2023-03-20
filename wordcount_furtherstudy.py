def tokenize(filename):
    """Create a list of words from the filename text"""

    #create an empty list variable
    retval = []
    #open the file
    data = open(filename)
    #iterate through lines from the file to clean it up
    for line in data:
        spaces_gone = line.rstrip()
        words_list = spaces_gone.split(" ")

        for word in words_list:
            retval.append(word)
    #adding each word from each line to one list

    return retval
#print(tokenize("test.txt"))
    #return empty list variable

def count_words(words):
   """Count unique elements in list"""

   #create empty dictionary variable
   retval = {}
   #loop through the list argument
   for word in words:
   #create if statement, if word is NOT in empty dictionary, add key and set to one
        if word not in retval:
            retval[word] = 1
        else:
            retval[word] += 1
   #otherwise add 1
   #return empty dictionary variable
   
   return retval

#print(count_words(["apple", "berry", "cherry", "apple"]))

def print_word_counts(word_counts):
    """Print each key:value pair in a line"""

    for key, element in word_counts.items():
        print(key,element)

print_word_counts({'apple': 2, 'berry': 1, 'cherry': 1})