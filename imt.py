import random
import string

def randomString(target, matching_char_set):
	answer = ''
	for i in range(len(target)):
		if i in matching_char_set:
			answer += target[i]
		else:
			answer += random.choice(string.printable)
	return answer

def isMatching(string1, string2, matching_char_set):
	for i in range(len(string1)):
		if string1[i] == string2[i]:
			matching_char_set.add(i)
	return matching_char_set

def matchString(target):
	matching_char_set = set()
	trial = ''
	trial_num = 0
	while trial != target:
		trial_num += 1
		trial = randomString(target,matching_char_set)
		print ("Trial", trial_num)
		print (trial)
		matching_char_set = isMatching(target, trial, matching_char_set)

def main():
	matchString(input("Write any sentence you would like to match! "))

main()