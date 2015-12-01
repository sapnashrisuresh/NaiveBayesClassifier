#1. Convert label of each rating : >= 7 (positive) or <= 4 (negative)
#2. Add 1 to each feature
#3. Split the dataset randomly into two files (75% and 25%)
#4. Process each of those into development files without label
#5. Store the labels in separate files to compute the performance measure of the model

# To run this file, execute: (labelBow.feat-training sentiment data, sentiment_test.feat-test data file)
#python3 preprocess_imdb.py labeledBow.feat sentiment_test.feat


import sys,os,random
from collections import Counter

infile = sys.argv[1]
testfile=sys.argv[2]

def preprocessData():
	with open(infile,'r') as filein, open('./sentiment.nb.in', 'w') as fileout:
		for line in filein.readlines(): 
			words=line.split(' ')
			firstline = True 
			for word in words:
				if firstline==False:
					x=word.split(':')[0]
					y=int(x)+1
					fileout.write( word.replace( x, ' '+str(y), 1) )
				if firstline:
					if int(word)>=7:
						fileout.write('POSITIVE')
					if int(word)<=4:
						fileout.write('NEGATIVE')
					firstline=False
		filein.close()
		fileout.close()

def preprocessTest():
	with open(testfile,'r') as filein, open('./sentiment_test_update.feat', 'w') as fileout:
		for line in filein.readlines(): 
			words=line.split(' ')
			firstword=True
			for word in words:
				if(firstword==False):
					x=word.split(':')[0]
					y=int(x)+1
					fileout.write( word.replace( x, ' '+str(y), 1) )
				else:
					x=word.split(':')[0]
					y=int(x)+1
					fileout.write( word.replace( x, str(y), 1) )
					firstword=False

		filein.close()
		fileout.close()


def readtrainingdata():
	with open('./sentiment.nb.in','r') as filein:
		trainingdata=[]
		for line in filein.readlines(): 
			trainingdata.append(line)		
		return trainingdata


def randomdataselection(trainingdata):
	with open('./sentiment.train75.in','w') as train75, open('./sentiment.train25.in','w') as train25, open('./sentiment.test75.in','w') as test75, open('./sentiment.test25.in','w') as test25, open('./sentiment.reference75.out','w') as ref75, open('./sentiment.reference25.out','w') as ref25:
		random.shuffle(trainingdata)
		size=len(trainingdata)
		size75=(len(trainingdata)*75)/100
		size25=size-int(size75)

		train_data = trainingdata[:int(size75)]
		test_data = trainingdata[-int(size25):]

		for line in train_data:
			train75.write(str(line))
			writeline=str(line).split(' ',1)[1]
			ref75.write(str(line).split(' ',1)[0]+'\n')
			test75.write(writeline)
		for line in test_data:
			train25.write(str(line))
			writeline=str(line).split(' ',1)[1]
			ref25.write(str(line).split(' ',1)[0]+'\n')
			test25.write(writeline)

def main():
	preprocessData()
	preprocessTest()
	trainingdata=readtrainingdata()
	randomdataselection(trainingdata)

if __name__ == "__main__": main()