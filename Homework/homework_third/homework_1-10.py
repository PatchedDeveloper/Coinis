import math
import random
import re

# Coinis_homework_3 by Danila Kardasehvskii

# Domaći zadatak 3


# ----------------------------------------------------------------
# TASK 1

def get_words_with_end_letter(words,key):

    split_sentences = re.split(r"[.!?]", words)[:-1]
    new_array_with_words = []

    # first cycle
    for i in split_sentences:
        words = i.split()
        print(words)

        time_array = []
        # second cycle
        for j in words:
            if j[-1] == key:
                time_array.append(j)
        time_array.append(len(time_array))
        time_array = tuple(time_array)    
        new_array_with_words.append(time_array)
    print(new_array_with_words)

get_words_with_end_letter(
    input("Enter Text: ")
    input("Enter Key: ")
)

# ----------------------------------------------------------------
# TASK 2


