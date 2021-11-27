import json
from difflib import get_close_matches

# loading data from a JSON file
data = json.load(open("data.json"))

# a function that finds a definition
def give_definition(w):
	w = w.lower()
	if w in data:
		return data[w]
	elif w.upper() in data:	#for abbreviations
		return data[w.upper()]
	elif w.title() in data:	#for words starting with a capital letter
		return data[w.title()]
	elif len(get_close_matches(w, data.keys())) > 0:
		answer = input("Did you mean %s? If yes, type Y; if no, type N:\n " % get_close_matches(w, data.keys(), cutoff = 0.8)[0])
		if answer == "Y":
			return data[get_close_matches(w, data.keys(), cutoff = 0.8)[0]]
		elif answer == "N":
			return "The word doesn't exist. Please double check it."
		else:
			return "We couldn't figure out what you were trying to say. Please give it another shot."
	else:
		return "The word doesn't exist. Please double check it."

input_word = input("Enter word:\n")
output = give_definition(input_word)
if type(output) == list:		#in case of many definitions
	for item in output:
		print(item)
else:				#in case of one definition
	print(output)