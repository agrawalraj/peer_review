#####################################################################################################
# IN BASH
#####################################################################################################
# Convert xlsx file to csv
# Doing this for only one file right now - will eventually automate to do for all sheets, regardless of whether for colony or coulter data
# xlsx2csv ./Bishayee\ Colony\ Counts\ 10.27.97-3.8.01.xlsx > data1.csv
#####################################################################################################
# IN PYTHON
import csv
#####################################################################################################
# Determine the column postition of the headings you want; function takes in the imported data list and the vector of potential heading (as strings) which depends on whether you're looking for colony or coulter count data.
def det_heading_idx(listData, headingsVec):
	cid = 'False'
	row = 0
	while cid == 'False':
		if(any(i for i in headings1 if i in testdata1[row])):
			col1 = testdata1[row].index([i for i in headings1 if i in testdata1[row]][0])
			cid = 'True'
		else:
			row = row+1
	return(col1, row)
#####################################################################################################
# Determine whether we're working with colony count or Coulter count data; this will depend on the data file and the specific type of test we're doing.
# Note: By finding out which header represents count or colony one, we can assume that the second and third instances of the triplicate measurments will immediately follow.
def det_datatype(dataType):
	if(dataType == 'colony'):
		# For colony data, columns are titled either "c#" or "col#" or "COL#"
		headings1 = ['col1', 'c1', 'COL1']
	if(dataType == 'coulter'):
		# the coulter count data is titled the following
		headings1 = ['count1', 'COU1', 'COUNT1']
	return(headings1)
#####################################################################################################
# Extract the data from the csv into a list of lists; each list represents a measurement.
def extract_data(dataPath, dataType='colony'):
# dataType should be either 'colony' or 'coulter'
	with open(dataPath, 'rb') as csvfile:
		# read the csv file
		testdata = csv.reader(csvfile)
		testdata=list(testdata)
		# determine the number of columns in the csv file
	nrow=len(testdata)
	ncol=len(testdata[0])
	# extract the data from the columns that matter, from each row.
	# Determine the data type (colony or coulter)
	headings = det_datatype(dataType)
	col1index, headerRow = det_heading_idx(testdata, headings)
	for i in range(headerRow+1, nrow):
		testdata[i] = testdata[i][col1index:col1index+4]
	return(testdata)
#####################################################################################################

