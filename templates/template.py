
import csv
import sys
import time
import random
import fileinput


""" 
	Created August 23, 2016; Updated April 26, 2017

	@author: Evan Thompson [ethom7]

	Program will create random data for testing purposes. 
	Specify the number of rows and columns of data.
	Accepts an input file as listed in INPUT_RESOURCE.
	Outputs data to OUTPUT_RESOURCE. 

"""

##--Vars---##
INPUT_RESOURCE = "data/NST-EST2015-alldata.csv" #"data/20k.txt"
INPUT_DELIMITER = ','
OUTPUT_RESOURCE = "documentfile.txt"
DESIRED_ROWS = 10000
DESIRED_COLUMNS = 3000


current_time = time.strftime("%m %d %Y-%H %M %S")
current_date = time.strftime("%m-%d-%Y")


##--Functions--##


"""
	Function will import a csv or textfile as a list.
	@param	file1: a string with the location of a delimited file.
			delim: a string containing a delimiter, typically a comma ',', space ' ', 
					or other specified entry
"""
def get_csv(file1, delim):
	returnlist = []
	with open(file1, 'U') as csvfile:
		freader = csv.reader(csvfile, delimiter=delim, quotechar='"', quoting=csv.QUOTE_MINIMAL)
		for row in freader:
			returnlist.append(row)

	return returnlist


##--Helper-Functions--##

def assembledictionary(header, data):

	returndictionary = {}

	columnlist = []

	## create a list of values for each column
	for col in range(len(data[0])):
		templist = []
		for row in range(len(data)):
			templist.append(data[row][col])

		columnlist.append(templist)


	# accept input of a row, index is across columns
	for x in range(len(header)):

		returndictionary[header[x]] = columnlist[x]

	return returndictionary


##--Main--##

def main():

	## Run timers
	start_time = time.time()
	print "Starting at %s..." % current_time

	
	## Function call with timer
	print "Doing functions..."
	function_start = time.time()

	datalist = get_csv(INPUT_RESOURCE, INPUT_DELIMITER)

	## datalist contains each row of the data sheet. 
	## Top row is the header, which will be the keys for the output dict, 
	## value is a list of values for each row.
	datadict = assembledictionary(datalist[0], datalist[1:])

	#print datadict

	function_end = time.time() - function_start
	print "Function processing time %.4f seconds" % (function_end,)

	end_time = time.time() - start_time
	print "%.4f seconds" % (end_time,)

if __name__ == '__main__':
	status = main()
	sys.exit(status)