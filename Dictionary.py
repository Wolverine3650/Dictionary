import json
from difflib import get_close_matches

collection = json.load(open("collection.json"))

def lookup(word):
    word = word.lower()
    if word in collection:
        return collection[word]
    elif len(get_close_matches(word, collection.keys())) > 0:
        yn = input("Are you looking for the word %s ? Enter Y for Yes or N for No: " % get_close_matches(word, collection.keys())[0])
        if yn == "Y" or yn=="y":
            return collection[get_close_matches(word, collection.keys())[0]]
        elif yn == "N" or yn=="n":
            return "Word not found. Please try again."
        else:
            return "Please enter either Y or N"
    elif len(get_close_matches(word, collection.keys())) == 0:
    	return "No such word Exists,Kindly Check Spelling!"
    
print('\n** THE PYTHON ENGLISH DICTIONARY **\n')
while (1):
	s=input("Enter :"+"\n"+"1 for Searching"+"\n"+"2 for Exit"+"\n")
	if(s=='1'):
		word = input("Enter word: ")
		output = lookup(word)
		if type(output) == list:
			for item in output:
				print(item)
		else:
			print(output)
	elif(s=='2'):
		break
	else:
		print("Invalid Option!!!")
		break