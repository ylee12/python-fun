"""
Given n number of strings with puntuations. Find words with top 5 occurance from these given strings.
Example: "This is a book.",
    "That is a chicken.",
    "That is a pen!!",
    "What are these?",
    "I am a student.",
    "I am a men!",
    "This is so good, and that is even better!! ",
    "Nothing is going to change our determination for success."
"""

import string
import re
import logging

def my_func(*args):
    """
    accept n number of strings as arguments.
    parse the string and return a dictionary with number of time each word appears in the sentences
    """

    punctuations = string.punctuation
    punctuations = '[' + punctuations + ']'
    my_dict = {}


    for i in args:

        logging.debug(f"Sentence: {i}")

        # remove all punctuation
        words = re.sub(punctuations, "", i).split()

        logging.debug(f"Words: {words}")
        for word in words:
            word = word.lower()
            if word not in my_dict:
                my_dict.update({word: 1})
            else:
                count = my_dict[word] + 1
                #count += 1
                my_dict.update({word: count})

        logging.debug(f"my_dict: {my_dict}")

    for k, v in my_dict.items():
        logging.info(f"{k} = {v}")

    return my_dict

def print_top_n(s, d, n):
    """
    print the top n word occurance
    """

    # get the iterable with index 
    enum_obj = enumerate(s)

    print(f"The top {n} word(s) by occurance is/are:")
    for index, ele in enum_obj:
        if index > n-1:
            break
        print(f"{ele}:{d[ele]}")

    

# set the logging to debug level
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

# set the logging to ERROR level
#logging.basicConfig(level=logging.ERROR, format="%(message)s")

d = my_func("This is a book.",
    "That is a chicken.",
    "That is a pen!!",
    "What are these?",
    "I am a student.",
    "I am a men!",
    "This is so good, and that is even better!! ",
    "Nothing is going to change our determination for success.")

#use the built-in sorted() method to sort a dictionary by value
#return a list of sorted elements
s = sorted(d, key=d.__getitem__, reverse=True)

#use the built-in sorted() method to sort a dictionary by key
#return a list of sorted elements
#s = sorted(d)

# print the top n word occurance
print_top_n(s, d, 5)

print("\nPrint top 3000 words(if there are any)")
print_top_n(s, d, 3000)