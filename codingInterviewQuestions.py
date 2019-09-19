#CODING INTERVIEW QUESTIONS IN PYTHON------------#
#My methods may not be the best or most efficient#
#------------------------------------------------#

#-------------#
#---SORTING---#
#-------------#

#1. HOW DO YOU FIND MISSING NUMBER IN SORTED ARRAY?#
def findMissingFromArray(array):
	y=1 #Difference Check. This is how we determine if we have multiple missing values
	for x in range(len(array)):
		if (x+y) != array[x]:
			print ("Missing number is %d" % (array[x]-1))
			y+=1 #Because we found a missing number, the difference check will have to be incremented

'''
MAIN FUNCTION
-------------
ourArray = [1,2,3,5,6,7,8,10]
findMissingFromArray(ourArray)
'''

#2. HOW DO YOU FIND DUPLICATE NUMBER?#
def findDupInArray(array):
	tempArray = []
	for x in range(len(array)):
		if array[x] not in tempArray:
			tempArray.append(array[x])
		else:
			print ("Duplicate found: %d @ index #%d" % (array[x], x))

'''
MAIN FUNCTION
-------------
ourArray = [1,2,4,5,5,6,7,7,7,8]
findDupInArray(ourArray)
'''

#3. HOW DO YOU FIND THE LARGEST AND SMALLEST IN AN UNSORTED ARRAY?
#Sorting and using the min/max functions are not allowed

def findMinMaxArray(array):
	min, max = array[0], array[0]
	for x in range(len(array)):
		if array[x] < min:
			min = array[x]
		if array[x] > max:
			max = array[x]

	print ("Largest value: %d\nSmallest value: %d" % (max, min))

'''
MAIN FUNCTION
-------------
ourArray = [545,16,14,6,1,6,81,65]
findMinMaxArray(ourArray)
'''

#4. HOW DO YOU FIND ALL PAIRS OF AN INTEGER ARRAY WHOSE SUM IS EQUAL TO X?# !!!!!!!!!!!!!!!!OPTIMIZE
def findPairsSumToX(array, target):
	pairList = []
	for y in range(len(array)):
		for z in range(y, len(array)):
			if array[y] + array[z] == target:
				pairList.append([array[y], array[z]])
				print ("Pair found: %d & %d" % (array[y], array[z]))
			z += 1
		y+=1

	print (pairList)

'''
MAIN FUNCTION
-------------
ourArray = [16,51,19,84,13,2,8,14,-57]
x = 27
findPairsSumToX(ourArray, x)
'''

#5. HOW IS AN INTEGER ARRAY SORTED IN PLACE USING QUICKSORT?#
#Recursion!
def splitArray(array, low, high):
	i = (low-1)
	pivot = array[high]

	for j in range(low, high):
		if array[j] <= pivot:
			i+=1
			array[i],array[j] = array[j],array[i] #easy swap

	array[i+1], array[high] = array[high], array[i+1] #swap these now that you are stopped
	return (i+1)

def quickSortArray(array, low, high): 
	if low < high:
		index = splitArray(array, low, high)
		quickSortArray(array,low,index-1)  #sorting each split
		quickSortArray(array,index+1,high) #sorting each split
'''
MAIN FUNCTION
-------------
ourArray = [9,6,14,91,35,31,67,16,61]
n = len(ourArray) - 1
print ("Array initially:\n%ls"%(ourArray))
quickSortArray(ourArray, 0, n)
print ("Array quick sorted:\n%ls"%(ourArray))
'''

#6. HOW DO YOU REVERSE AN ARRAY?#
def reverseArray(array):
	i = 0 #iterator, starting with index 0
	j = len(array)-1 #this is the index of the last element. We will decrement it
	print ("Array initially:\n%ls"%(array) )
	while i < j:
		array[i], array[j] = array[j],array[i] #swap these fools
		i += 1 #move right
		j -= 1 #move end index down
	print ("Array reversed:\n%ls"%(array))

'''
MAIN FUNCTION
-------------	
ourArray = [9,6,14,91,35,31,67,16,61,37]
reverseArray(ourArray)
'''

#7. HOW WOULD YOU REMOVE DUPLICATES?#
#Your first thought may be to remove the duplicate while searching.
#This will throw you out of range, so we will do it another way.
#After the duplicateList is populated, we will remove the elements from the array.
def removeDupsArray(array):
	tempArray = []
	duplicateList = []
	for x in range(len(array)):
		if array[x] in tempArray:
			duplicateList.append(array[x])
			print ("Duplicate found: %d @ index #%d" % (array[x], x))
		if array[x] not in tempArray:
			tempArray.append(array[x])

	for y in duplicateList:
		if y in array:
			array.remove(y)

	print ("Duplicate List: %ls" % (duplicateList))
	print ("Array with duplicates deleted: %ls" % (array))
	
'''
MAIN FUNCTION
-------------	
ourArray = [1,2,3,4,4,4,5,5,6,7,8,8,10]
removeDupsArray(ourArray)
'''

#-------------#
#---STRINGS---#
#-------------#

#1. HOW DO YOU PRINT DUPLICATE CHARACTERS FROM A STRING?#
#Doesn't take into account capitalization.
def printDupsFromString(theString):
	stringDict = {}
	duplicateDict = {}
	for c in theString:
		if c not in stringDict and c != ' ':#last part if spaces aren't considered characters
			stringDict[c] = 1
		elif c in stringDict and c != ' ':
			stringDict[c] += 1

	for x in stringDict:
		if stringDict[x] > 1:
			duplicateDict[x] = stringDict[x] - 1

	print ("Extra characters %ls" % (duplicateDict))

'''
MAIN FUNCTION
-------------
theString = "This is a string"
printDupsFromString(theString)
'''

#2. HOW DO YOU CHECK TO SEE IF TWO STRINGS ARE PALINDROMES?#
#This will be similar #7, in that we will use an index to run from the end of one item
#Watch out for things like instructions to ignore case/numbers/symbols
#Use string1 = string1.lower() and make a dict and use it for translation if you need to 
#get rid of special symbols. Iterating through the string and replacing characters is too slow
def checkPal(one,two):
	palBool = True

	d = len(two)-1 #index of last char in string #2
	if len(one) == len(two):
		for c in xrange(len(one)-1):
			if one[c] == two[d]:
				d -= 1
			else:
				palBool = False
	else:
		palBool = False

	return palBool

'''
MAIN FUNCTION
-------------
string1 = "23hf9hd9h"
string2 = "29hf29n2h"
string3 = "h9dh9fh32"
print ("String 1: %s / String 2: %s / Palindrome Check: %s" % (string1, string2, checkPal(string1, string2)))
print ("String 1: %s / String 3: %s / Palindrome Check: %s" % (string1, string3, checkPal(string1, string3)))
print ("String 2: %s / String 3: %s / Palindrome Check: %s" % (string2, string3, checkPal(string2, string3)))
'''

#3. HOW DO YOU CHECK THE FIRST NON-REPEATED CHARACTER OF A STRING?
#Compare two characters. Iterate through chars in string. If it ain't the same as the previous, you've done it!


def firstOriginalCharString(theString):
	prevChar = theString[0]

	for char in theString:
		if char != prevChar:
			print ("First non-repeated char is: " + char + "\n")
			break


'''
MAIN FUNCTION
-------------
theString = "llama"
firstOriginalCharString(theString)

'''

#-------------#
#----OTHER----#
#-------------#

#1. GIVEN LOWER LEFT AND UPPER RIGHT COORDINATES OF 2 RECTANGLES, HOW DO YOU FIGURE THE AREA OF OVERLAP?
#If statement determines if there is overlap. This makes sure you don't get any values when there are not. The min - max algorithm would still produce
#values even though they aren't relevant in the case of no overlap.


def areaOfOverlap(r1,r2):
	
	if r2.lowerX in range(r1.lowerX,r1.upperX) or r1.lowerX in range(r2.lowerX,r2.upperX) and r2.lowerY in range(r1.lowerY, r1.upperY) or r1.lowerY in range(r2.lowerY, r2.upperY):
		width = abs(min(r1.upperX, r2.upperX) - max(r1.lowerX, r2.lowerX))
		height = abs(min(r1.upperY, r2.upperY) - max(r1.lowerY, r2.lowerY))
		return width * height
	else:
		return False



'''
MAIN FUNCTION
-------------
class r:
	def __init__(self, lx, ly, ux, uy):
		self.lowerX = lx
		self.lowerY = ly
		self.upperX = ux
		self.upperY = uy
	def printCoordinates(self):
		(print "Coordinates are (" + str(self.lowerX) + "," + str(self.lowerY) + ")(" + str(self.upperX) + "," + str(self.upperY) + ")\n")

rect1 = r(2,1,5,5)
rect2 = r(3,2,5,7) 
rect3 = r(3,0,4,1)
rect4 = r(-3,4,4,4)

print (areaOfOverlap(rect3, rect4)#Test case 1 is rect1, rect2 = 6 ||| Test case 2 is rect3, rect4 = False)

'''

#2. HOW MANY WAYS ARE THERE TO DECODE THIS MESSAGE?
#Recursion is needed here. Without memoization, this problem is O(n^k), with it, it becomes O(n)

def recursionHelper(theString, k, memo):
	if k==0:
		return 1

	i = len(theString) - k
	if theString[i] == '0':
		return 0

	if memo[k] != None:
		return memo[k]

	result = recursionHelper(theString, k-1, memo)
	if k >=2 and int(theString[i:i+2]) <= 26:
		result += recursionHelper(theString, k-2, memo)
	memo[k] = result
	return result

def numWays(theString):
	memo = [None for i in range(len(theString) + 1)]
	return recursionHelper(theString, len(theString), memo)

'''
MAIN FUNCTION
-------------
s1 = "12345" 			#result = 3
s2 = "296678"			#result = 1
s3 = "044"				#result = 1
s4 = ""					#result = 0
s5 = "297529234729384"	#result = 2
print (numWays(s5))s
'''
