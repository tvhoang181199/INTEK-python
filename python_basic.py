import math
import string

import pygame

#Waypoint 1
def hello(name):
	name = name.strip()
	return "Hello " + name + "!"

#Waypoint 2
def calculate_hypotenuse(a, b):
	return math.sqrt(a**2 + b**2)

#Waypoint 3
def are_all_conditions_true(conditions):
	if len(conditions) == 0:
		return None
	for i in range(0,len(conditions)):
		if conditions[i] == False:
			return False
	return True

#Waypoint 4
def is_a_condition_true(conditions):
	if len(conditions) == 0:
		return None
	for i in range(0,len(conditions)):
		if conditions[i] == True:
			return True
	return False

#Waypoint 5
def filter_integers_greater_than(l, n):
	result = []
	for i in range(0,len(l)):
		if l[i] > n:
			result.append(l[i])
	return result

#Waypoint 6
def value(n):
	return n[1]

def sort(l):
	return sorted(l, key = value)

def find_cheapest_hotels(hotels, maximum_daily_rate):
	result = []
	max = 0
	min = 0
	for i in range(0,len(hotels)):
		if hotels[i][1] <= maximum_daily_rate:
			if len(result) == 0:
				max = min = hotels[i][1]
				result.append(hotels[i][0])
			elif hotels[i][1] >= max:
				max = hotels[i][1]
				result.append(hotels[i][0])
			elif hotels[i][1] < min:
				result.insert(0, hotels[i][0])
	return result

#Waypoint 7
def calculate_euclidean_distance_between_2_points(p1, p2):
	return math.sqrt(pow(p1[0]-p2[0],2) + pow(p1[1]-p2[1], 2))

#Waypoint 8
def calculate_euclidean_distance_between_points(l):
	if len(l)<2:
		raise ValueError("The list MUST contain at least 2 points")
	sum = 0
	for i in range(0, len(l)-1):
		sum += calculate_euclidean_distance_between_2_points(l[i], l[i+1])
	return sum


#Waypoint 9
def capitalize_words(s):
	if s == None:
		raise TypeError("Not a string")
	s = s.strip()
	temp1 = []
	result = ''
	temp1 = s.split(' ')
	for i in range(0,len(temp1)):
		if temp1[i] != '':
			result += str(temp1[i].capitalize() + ' ')
	result = result.strip()
	return result


#Waypoint 10
def uppercase_lowercase_words(s):
	if isinstance(s, str) == False:
		raise TypeError("Not a string")
	if s.isspace() == True:
		return ''
	if s == None:
		return None
	temp = []
	result = ''
	temp = s.split(' ')
	for i in range(0,len(temp)):
		if i % 2 == 0:
			result += str(temp[i].upper() + ' ')
		else:
			result += str(temp[i].lower() + ' ')
	result = result.strip()
	return result


#Waypoint 11
def factorial(n):
	if isinstance(n, int) == False:
		raise TypeError("Not an integer")
	if n < 0:
		raise ValueError("Not a positive integer")
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return factorial(n - 1) * n

#Waypoint 12
def char_to_int(s):
	if isinstance(s, str) == False:
		raise TypeError("Not a string")
	if len(s) >= 2 or (s >= 'a' and s < 'z') or (s >= 'A' and s <= 'Z'):
		raise ValueError("Not a single digit")
	return int(ord(s)-48)

#Waypoint 13
#10^i
def tenpoweri(i):
	result = 1
	for i in range(0,i):
		result *= 10
	return result

def string_to_int(s):
	if isinstance(s, str) == False:
		raise TypeError("Not a string")
	if s[0] == '-':
		raise ValueError("Not a positive integer string expression")
	for i in range(0,len(s)):
		if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
			raise ValueError("Not a positive integer string expression")
	result = 0
	for i in range(0,len(s)):
		result += char_to_int(s[i])*tenpoweri(len(s)-i-1)
	return result

#Waypoint 14
def is_palindrome(value1):
	value = str(value1)
	temp = ''
	for i in range(0,len(value)):
		if (value[i] >= 'a' and value[i] <= 'z') or (value[i] >= 'A' and value[i] <= 'Z') or (value[i] >= '0' and value[i] <= '9'):
			temp += value[i]
	for i in range(0,(len(temp)//2)-1):
		if (ord(temp[i]) != ord(temp[len(temp)-1-i])) and (ord(temp[i]) + 32 != ord(temp[len(temp)-1-i])) and (ord(temp[i]) - 32 != ord(temp[len(temp)-1-i])):
			return False
	return True

#Waypoint 15
def roman_numeral_to_int(s):
	if isinstance(s, str) == False:
		raise TypeError("Not a string")
	for i in range(0,len(s)):
		if not s[i] in ['N', 'I', 'V', 'X', 'L', 'C', 'D', 'M']:
			raise ValueError("Not a Roman numeral")
	if s == 'N':
		return 0
	result = 0
	for i in range(0,len(s)-1):
		if s[i] == 'I':
			if s[i+1] == 'V' or s[i+1] == 'X':
				result -= 1
			else:
				result += 1
		if s[i] == 'V':
			result += 5
		if s[i] == 'X':
			if s[i+1] == 'L' or s[i+1] == 'C':
				result -= 10
			else:
				result += 10
		if s[i] == 'L':
			result += 50
		if s[i] == 'C':
			if s[i+1] == 'D' or s[i+1] == 'M':
				result -= 100
			else:
				result += 100
		if s[i] == 'D':
			result += 500
		if s[i] == 'M':
			result += 1000
	Roman_Dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	result += Roman_Dict[s[len(s)-1]]
	return result

#Waypoint 16
def play_melody(melody, sound_basedir):
	pygame.init()
	keys = {1:'c', 2:'d', 3:'e', 4:'f', 5:'g', 6:'a', 7:'b'}
	rv_keys = {'c':1, 'd':2, 'e':3, 'f':4, 'g':5, 'a':6, 'b':7}
	for i in range(0,len(melody)):
		# if '#' in melody[i].lower():				#Raise an exception
		# 	raise KeyError(melody[i].lower())

		result = ''
		temp = str(melody[i].lower())
		temp1 = ''
		if '#' in temp:
			temp1 = str(keys[rv_keys[temp[0]]+1] + 'b' + temp[2])
			result = str(sound_basedir + '/' + temp1 + ".ogg")

		else:
			result = str(sound_basedir + '/' + 	temp + ".ogg")
		sound = pygame.mixer.Sound(result)
		channel = sound.play(0,1600,0)
		sound = pygame.time.delay(400)
		print(result)


