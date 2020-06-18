import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
        '''for i in data[word]:
            print(i + "\n")'''
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        return "Did you mean %s instead? " % get_close_matches(word, data.keys())[0]
    else:
        return "The word doesn't exist. Please double check it"

word = input("Enter a word: ")

print(translate(word))