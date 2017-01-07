import os.path
import csv
import fnmatch

# Register file dialect
csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)

# User Introduction
print "Welcome to the Visible World connection portal reference"
print ""
print "In order to use this program, you will be required to provide a pipe-seperated .txt file"
print ""
full_file_path = raw_input("Please enter the complete file path for your file: ")

# Verify that file exists
def verifyFile():
    if os.path.isfile(full_file_path):
        print "Verified file exists"
    else:
        print "No Such File"  

# Verify file is proper type
def verifyType():
        if fnmatch.fnmatch(full_file_path, '*.txt'):
            print "Verified proper file type"
        else:
            print "This is not the proper file format" 

# Read and print file to console
def fileReader():
    with open(full_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
#        for row in csv.DictReader(full_file_path, dialect='piper'):
        for row in reader:
            print row

# Read or query file
def readNow():
    userAnswer = raw_input("Would you like to read the file now? (y/n)")
    if userAnswer == 'y':
        fileReader()
    elif userAnswer == 'n':
        userQueryAnswer = raw_input("Would you like to query the connection file? (y/n)")
        if userQueryAnswer == 'y':
            queryNow()
        elif userQueryAnswer == 'n':
            userAddRow = raw_input("Would you like to add a row to the connection file? (y/n)")
            if userAddRow =='y':
                addRow()
            elif userAddRow =='n':
                print "You have no more options.  Goodbye"
            else:
                print "That is not an acceptable answer"
                readNow()
        else:
            print "That is not an acceptable answer"
            readNow()
    else:
        print "That is not an acceptable answer"
        readNow()

# Query the user provided file
def queryNow():
    print "You are about to query the file for best possible connection string"
    print "You will need to provide the Source and Target hosts systems for your data"
    sourceData = raw_input('What is your source system?')
    targetData = raw_input('What is your target system?')
#    with open(full_file_path, 'r') as queryfile:
    queryFile = csv.DictReader(open(full_file_path))
    for row in queryFile:
        Host1 = str(row["Host 1"])
        Host2 = str(row["Host 2"])
        if Host1 == sourceData and Host2 == targetData:
            print row


# Add a row to the user provided file
def addRow():
    print 'So far so good - add row'

def main():
    verifyFile()
    verifyType()
    readNow()

main()
