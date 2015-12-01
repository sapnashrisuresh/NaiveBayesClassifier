#Convert the email data to a single file with features and values and split the data randomly in to two files

# To run this file, execute: (enron.vocab-vocab file of spam data)
#python3 preprocess_email.py enron.vocab spam.nb.in spam_test.nb.in

import sys,os,random
from collections import Counter

vocabfile = sys.argv[1]
outfile = sys.argv[2]
outfiletest = sys.argv[3]

#get dictionary of email vocab and create training data for each file
def vocabDictioanry():
	with open(vocabfile,'r',encoding='latin1') as vocab:
		dict = {}
		num=1
		for line in vocab.readlines():
			dict[line.rstrip('\n')]=num
			num=num+1
		return dict

def preprocessTrain(dict):
	rootDir = '.'
	for dirName, subdirList, fileList in os.walk(rootDir):
	    #print('Found directory: %s' % dirName)
	    for fname in fileList:
	    	if fname.endswith('am.txt'):
	    		with open(os.path.join(dirName, fname),'r',encoding='latin1') as filein, open(outfile, 'a') as fileout:
	    			cnt = Counter()
	    			for line in filein.readlines(): 
	    				words=line.split(' ')
	    				for word in words:
	    					cnt[word.rstrip('\n')] += 1
	    			newdict = {}
	    			for i in cnt:
	    				if(dict.get(i,0)>0):
	    					key=dict[i]
	    					value=cnt[i]
	    					newdict[key]=value
	    				else:
	    					continue
	    			firstword=True
	    			if fname.endswith('spam.txt'):
	    				label='SPAM'
	    			else:
	    				label='HAM'
	    			for key in sorted(newdict):
	    				if firstword==False:
	    					fileout.write(' '+str(key)+':'+str(newdict[key]))
	    				else:
	    					fileout.write(label)
	    					fileout.write(' '+str(key)+':'+str(newdict[key]))
	    					firstword=False
	    			fileout.write('\n')
	    		filein.close()

def preprocessTest(dict):
	rootDir = './spam_or_ham_test'
	for dirName, subdirList, fileList in os.walk(rootDir):
	    #print('Found directory: %s' % dirName)
	    for fname in fileList:
	    	if fname.endswith('.txt'):
	    		with open(os.path.join(dirName, fname),'r',encoding='latin1') as filein, open(outfiletest, 'a') as fileout:
	    			cnt = Counter()
	    			for line in filein.readlines(): 
	    				words=line.split(' ')
	    				for word in words:
	    					cnt[word.rstrip('\n')] += 1
	    			newdict = {}
	    			for i in cnt:
	    				if(dict.get(i,0)>0):
	    					key=dict[i]
	    					value=cnt[i]
	    					newdict[key]=value
	    				else:
	    					continue
	    			firstword=True
	    			for key in sorted(newdict):
	    				if firstword==False:
	    					fileout.write(' '+str(key)+':'+str(newdict[key]))
	    				else:
	    					fileout.write(str(key)+':'+str(newdict[key]))
	    					firstword=False
	    			fileout.write('\n')
	    		filein.close()

def readtrainingdata():
	with open(outfile,'r') as filein:
		trainingdata=[]
		for line in filein.readlines(): 
			trainingdata.append(line)		
		return trainingdata


def randomdataselection(trainingdata):
	with open('./spam.train75.in','w') as train75, open('./spam.train25.in','w') as train25, open('./spam.test75.in','w') as test75, open('./spam.test25.in','w') as test25, open('./spam.reference75.out','w') as ref75, open('./spam.reference25.out','w') as ref25:
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
	dict=vocabDictioanry()
	preprocessTrain(dict)
	preprocessTest(dict)
	trainingdata=readtrainingdata()
	randomdataselection(trainingdata)

if __name__ == "__main__": main()