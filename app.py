import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def main():
    word = input("Enter word: ")
    output  = translate(word)
    
    if(type(output) == list):
        #It got a definition of definitions which is a list
        if(len(output) == 1):
            print("We found 1 definition.")
        else:
            print("We found {} definitions.".format(len(output)))
        for (i, item) in enumerate(output):
            print(str(i +1) + (". {}".format(item)))
    else:
        #It is and error which is a string.
        print(output)
    

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean {} instead?\nEnter Y if yes, or N if no: ".format(get_close_matches(w, data.keys())[0]))
        if yn.upper() == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.upper() == 'N':
            return "The word does not exist. Double check it and try again."
        else:
            return "We did not understand your query."
    else:
        return "The word does not exist. Double check it and try again."

if __name__=='__main__':main()