#!/usr/bin/env python
import re 

def sort_menu():
	"""This function serves as sorting menu"""
	print "\nCreate new or use existing array? (N or E)"
	option = raw_input("> ")
	if (option == "N"):
		array_list = create_array(1)
	else:
		array_list = [5, 2, 7, 4, 3, 1, 9, 6] # default arrays provided
		
	print "Your arrays of numbers are : ", array_list
	
	print """
		1. Bubble sort
		2. Selection sort
		3. Insertion sort
		4. Python built-in sorted() - default 
	"""
	option = raw_input("> ")
	if (option == "1"):
		bubble_sort(array_list)
	elif (option == "2"):
		selection_sort(array_list)
	elif (option == "3"):
		insertion_sort(array_list)
	else:
		print "Life made easy by built in : ", sorted(array_list)

def create_array(arraytype):
	"""This function creates new list of array numbers"""
	array_list = []
	print "Enter your set of numbers. Enter 'x' when done."
	while True:
		value = raw_input ("> ")
		if (value == 'x'):
			break
		if arraytype == 1: # Only number allowed in this list
			try:
				num = int(value)
			except ValueError:
				print "That's not a number."
			else:
				print "Adding %d to the list" % num
				array_list.append(num)
		else: # Accepts any alphanumber values in the list
			print "Adding %r to the list" % value
			array_list.append(value)
			
	return array_list

def bubble_sort(array_list):
	"""This function performs bubble sort on list of arrays"""
	print "Bubble sorting this array..."
	swapped = True
	j = 0
	swapcnt = 0
	while (swapped):
		swapped = False
		j+=1
		for i in range(0, len(array_list)-1):
			if (array_list[i] > array_list[i+1]):
				temp = array_list[i]
				array_list[i] = array_list[i+1]
				array_list[i+1] = temp
				swapped = True
				swapcnt+=1
				print "New sorted arrays: ", array_list
	print "Total of %d swaps involved" % swapcnt

def selection_sort(array_list):
	"""This function performs selection sort on list of arrays"""
	print "Selection sorting this array..."
	swapcnt = 0
	for i in range(0, len(array_list)-1):
		mindex = i 
		for j in range(i+1, len(array_list)):
			if (array_list[j] < array_list[mindex]):
				mindex = j
		if (mindex != i):
			temp = array_list[i]
			array_list[i] = array_list[mindex]
			array_list[mindex] = temp
			swapcnt+=1
			print "New sorted arrays: ", array_list
	print "Total of %d swaps involved" % swapcnt

def insertion_sort(array_list):
	"""This function performs insertion sort on list of arrays"""
	print "Insertion sorting this array..."
	swapcnt = 0
	for i in range(1, len(array_list)):
		j = i
		while (j > 0 and (array_list[j-1] > array_list[j])):
			temp = array_list[j]
			array_list[j] = array_list[j-1]
			array_list[j-1] = temp
			j-=1
			swapcnt+=1
			print "New sorted arrays: ", array_list
	print "Total of %d swaps involved" % swapcnt

def file_reader():
	"""This function will read from the file and show the statistics required"""
	filename = raw_input("\nEnter filename: ")
	text = open(filename, 'r').read()
	words = text.split(' ')
	sentence = text.split('. ')
	wordcnt = len(words) 
	print "Total number of words : ", wordcnt
	print "Total number of sentence : ", len(sentence)
	longword = ""
	avgwordlen = 0
	wordabove3 = 0
	for i in range(0, len(words)):
		currword = words[i].strip(',')
		currword = currword.strip('. ')
		if (len(longword) < len(currword)): # Replace if current word is longest
			longword = currword
		
		avgwordlen = avgwordlen + len(currword) # Get total words length
		if (len(currword) > 3): # Get number of words with above 3 characters
			wordabove3 += 1

	print "Longest word : ", longword
	print "Average length of word used : %.2f " % (float(avgwordlen) / wordcnt)
	print "Numbers of words above 3 characters : ", wordabove3
	
def time_between():
	"""This function will get the minutes between 2 times"""
	print "Please enter time in 12:34AM or 12:34PM format."
	firsttime = raw_input("Enter first time : ").upper()
	secondtime = raw_input("Enter second time : ").upper()
	if (re.match(r'([0-9]+):([0-9][0-9])(AM|PM)', firsttime) and re.match(r'([0-9]+):([0-9][0-9])(AM|PM)', secondtime)):
		if firsttime.endswith("AM"):
			totalfirstmin = process_time(firsttime, "AM")
		elif firsttime.endswith("PM"):
			totalfirstmin = process_time(firsttime, "PM")
		if secondtime.endswith("AM"):
			totalsecmin = process_time(secondtime, "AM")
		elif secondtime.endswith("PM"):
			totalsecmin = process_time(secondtime, "PM")

		print "\nTotal minutes in between %s and %s are %d minutes" % (firsttime, secondtime, totalsecmin - totalfirstmin)
	else:
		print "Wrong time formats entered."
	
def process_time(time_str, time_abbr):
	"""This function will strip off the 'AM' or 'PM' and converts time to minutes"""
	time_str = time_str.rstrip(time_abbr)
	time = time_str.split(':')
	hour = int(time[0])
	if (time_abbr == "PM" and hour != 12):
		hour += 12
	minute = int(time[1])
	return minute + (hour * 60)
	
def largest_string():
	"""This function finds the largest string in an array of strings"""
	print "Type in any statement : "
	sentence = raw_input("> ")
	words = sentence.split(' ')
	longw1, longw2, longw3 = "", "", ""
	for i in range(0, len(words)):
		if len(words[i]) >= len(longw1):
			longw3, longw2, longw1 = longw2, longw1, words[i]
		elif len(words[i]) >= len(longw2):
			longw3, longw2 = longw2, words[i]
		elif len(words[i]) >= len(longw3):
			longw3 = words[i]
	
	print "3 largest strings are \'%s\', \'%s\', and \'%s\'" % (longw1, longw2, longw3)

def code_improve():
	"""This function just shows another way to write a code and run it"""
	print """
	Given below:
		function heightInCm(feet, inches)
		{
			feetAsInches = feet * 12
			totalInches = inches + feetAsInches
			cm = totalInches * 2.54
			return cm
		}
	
	This can be simplified to below:
		function heightInCm(feet, inches)
		{
			return (inches + (feet * 12)) * 2.54
		}
	or in Python as:
		def heightInCm(feet, inches):
			return (inches + (feet * 12)) * 2.54
	"""
	option = raw_input("Do you want to try on the new function (Y or N)? ")
	if (option == "Y"):
		feet = int(raw_input("Enter feet value or ft : "))
		inches = int(raw_input("Enter inches value or \'\"\' : "))
		print "This is equivalent to %r cm" % (heightInCm(feet, inches))

def heightInCm(feet, inches):
	return (inches + (feet * 12)) * 2.54

def odd_even_rounder():
	"""This function will take a float number and round it using odd-even rounding. 
	3.5 becomes 4; 6.5 becomes 6"""
	while True:
		numstr = input("Enter a float number : ")
		try:
			floatnum = float(numstr)
		except ValueError:
			print "This is not a float number!"
		else:
			intnum = int(numstr)
			decimalleft = floatnum - intnum
			# If integer component is odd, round up from 0.5;
			# If integer component is even, round up from more than 0.5
			if (decimalleft >= 0.5 and (intnum % 2) == 1) or \
				(decimalleft > 0.5 and (intnum % 2) == 0): 
				intnum += 1
			break

	print "Rounded integer of %.2f is %d" % (floatnum, intnum)

def swap_characters():
	"""This function will swap the case of each character in a string"""
	newstr = []
	string = raw_input("Enter a string : ")
	for char in string:
		if char.isupper():
			newstr.append(char.lower())
		elif char.islower():
			newstr.append(char.upper())
		else:
			newstr.append(char)
	
	print ''.join(newstr)
	
def find_nearest():
	"""This function will find the position of a given number given sorted array of number; 
	or if not found the position of next largest number"""
	print "\nCreate new or use existing array? (N or E)"
	option = raw_input("> ")
	if (option == "N"):
		array_list = create_array(1)
	else:
		array_list = [1, 6, 7, 9, 13] # provided array list
		
	array_list.sort()
	print "The array of numbers are ", array_list
	searchnum = int(raw_input("Enter number to find : "))
	orinum = searchnum
	matched = True
	while True:
		try:
			pos = array_list.index(searchnum)
		except ValueError:
			searchnum += 1 # increase search number by 1 to look in index
			matched = False
			if (searchnum <= max(array_list)):
				continue
			else: 
				print "%d NOT even exists within list. The largest number is %d" \
					% (orinum, max(array_list))			
				break
		else:
			if not matched:
				print "%d NOT exists in list. Next largest number is %d with index of %d " \
					% (orinum, array_list[pos], pos)
				matched = True
			else:
				print "%d exists in list with index of %d" % (searchnum, pos)
			break

def get_non_duplicate():
	"""This function will return out of list with duplicates, a new list without duplicates"""
	print "\nCreate new or use existing array? (N or E)"
	option = raw_input("> ")
	if (option == "N"):
		array_list = create_array(0)
	else:
		array_list = [1, 6, 5, "mary", "sean", 6, "peter", "mary"] # provided array list
	print "The duplicated array is ", array_list
	non_dup_list = []
	for i in range(0, len(array_list)):
		try:
			pos = non_dup_list.index(array_list[i]) 
		except ValueError: # Append to new list if no item yet exist in list
			temp = array_list[i]
			non_dup_list.append(temp)
		except IndexError: # Also append if no duplicate item found in old list 
			temp = array_list[i]
			non_dup_list.append(temp)
		else:
			print "Duplicate entry of %r found." % array_list[i]
	
	print "New non-duplicate list : ", non_dup_list 
	
def main_menu():
	"""This serves as the main menu for this program"""
	while True:
		print "-" * 50
		title = "Intellicentrics Programming Challenges"
		print title.center(50, ' ')
		print "-" * 50
		
		print """
		1. Sorting
		2. File reader
		3. Time between
		4. Largest string
		5. Improve this code
		6. Odd-even rounder
		7. Swap characters
		8. Find nearest
		9. No duplicate list
		"""
		option = raw_input("Choose from any number above or 'x' to exit : ")
		if option == "1":
			sort_menu()
		elif option == "2":
			file_reader()
		elif option == "3":
			time_between()
		elif option == "4":
			largest_string()
		elif option == "5":
			code_improve()
		elif option == "6":
			odd_even_rounder()
		elif option == "7":
			swap_characters()
		elif option == "8":
			find_nearest()
		elif option == "9":
			get_non_duplicate()
		elif option == "x":
			break
		else: continue
		raw_input("\nPress enter to continue...")
		print " " * 10
		
	print "\nThank you!", raw_input(" Enter to exit. ")

if __name__ == "__main__":
	print("Running Intellicentrics.py directly")
	main_menu()
#else:
#    print("one.py is being imported into another module")