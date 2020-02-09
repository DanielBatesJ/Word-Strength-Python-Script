import re
import operator

def main():
	dict={}

	#Replace with your text file path below
	path = "C:/Users/Danie/Desktop/New folder/UNT/2019 - Fall/CSCE 3110/HW1/Constitution.txt"
	
	#Change the value of maxNum to the number of results you want printed.	
	maxNum = 5

	#Add or remove words from this list to get more interesting results.
	boringWords = {'the', 'of', 'and', 'to', 'be', 'or', 'in', 'shall', 'by', 'a', 'for', 'any', 'as', 'have', 'such', 'may', 'which', 'not', 'no', 'from', 'on', 'this', 'all'}

	file_parse = open(path, 'r')
	for word in file_parse.read().split():
		word = re.sub('[!@#$,.]', '', word)
		word = word.lower()
		if word in dict and word not in boringWords:
			numUse = dict[word]
			dict[word] = numUse+1
		else:
			dict[word] = 1
	dict_sorted = sorted(dict.items(),key = operator.itemgetter(1),reverse = True)
	print("In this text file, the most used words are...")
	cnt = 0
	for i in dict_sorted:
		cnt += 1
		if cnt == maxNum + 1:
			break
		print(i)
main()