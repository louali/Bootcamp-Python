import sys

def text_analyzer(text):
    if text == None:
        return "What is the text to analyse?"
    array = [0,0,0,0,0]
    for c in text:
        array[0] += 1
        if (ord(c) > 64) & (ord(c) < 91):
            array[1] += 1
        if (ord(c) > 96) & (ord(c) < 123):
            array[2] += 1
        if (ord(c) == 33) | (ord(c) == 39) | (ord(c) == 46) | (ord(c) == 44) | (ord(c) == 63) | (ord(c) == 39):
            array[3] += 1
        if ord(c) == 32:
            array[4] += 1
    print("total = " + str(array[0]) + "Maj = " + str(array[1]) + " Min = " + str(array[2]) + " Ponct = " + str(array[3]) + " Spaces = " + str(array[4]))

# import sys
# import re


# def text_analyzer(text=None):
#     '''This function counts the number of upper characters, lower characters,
# punctuation and spaces in a given text.'''
#     if text is None:
#         text = input("What is the text to analyse?\n")

#     punc = re.findall(r"[!\"\#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~]", text)
#     lower = re.findall(r"[a-z]", text)
#     upper = re.findall(r"[A-Z]", text)
#     spaces = re.findall(r"[ ]", text)
#     print("The text contains", len(text), "characters:")
#     print("-", len(upper), "upper letters")
#     print("-", len(lower), "lower letters")
#     print("-", len(punc), "punctuations characters")
#     print("-", len(spaces), "spaces")
