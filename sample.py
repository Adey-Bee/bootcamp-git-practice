#Lodash for python
def unique(l):
	'''
	This function generate a list of unique values from l
	'''
	for value in l:
    		n = 0
    	for j in l:
        	if value == j:
            		n = 1
            
    		if n == 0:
       			 l.append(value)
	return l


def reverse(s):
	'''
	This function generates the reverse of s. s can be a string or a list. It returns the type given to it
	'''
	pass

def intersection(a,b):
	'''
	This function returns the intersection of a and b - A list of common elements between a and b
	'''
	pass


def generate(steps):
	pass

def parse_csv(csv_string):
	'''
	This function parses a CSV string as a list. The specification demands that the first row of data represents the column names
	'''
	pass

def frequency(needle, haystack):
	'''
	This function returns the number of times needle appears in haystack
	'''
	pass

def sort(l):
	'''
	This function returns a sorted version of l
	'''
	pass


def square(n):
    squared = n**2
    
    return squared
