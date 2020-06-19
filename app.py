import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]     
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        yerOrNo = input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(word, data.keys())[0])
        if yerOrNo == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yerOrNo == "N":
            return "The word doesn't exist. Please double check it!"
        else:
            return "We didnt understand your entry!"
    else:
        return "The word doesn't exist. Please double check it!"

def output(output):
    if type(output) == list:
        for i in output:
            print(i)
    else:
        print(output)
word = input("Enter a word: ")
output(output = translate(word))
