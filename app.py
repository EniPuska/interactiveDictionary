import json
from difflib import SequenceMatcher

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        SequenceMatcher(None, )
        return data[word]
        '''for i in data[word]:
            print(i + "\n")'''
    else:
        return "The word doesn't exist. Please double check it"

word = input("Enter a word: ")

print(translate(word))