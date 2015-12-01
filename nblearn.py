import sys

infile = sys.argv[1]
outfile = sys.argv[2]

def readtrainingdata():
	with open(infile,'r') as filein:
		trainingdata=[]
		for line in filein.readlines(): 
			trainingdata.append(line)
		return trainingdata

def calculateProbability(randomtraining):
	with open(outfile, 'w') as fileout:
		totalSize=len(randomtraining)
		totalPositive=0
		totalNegative=0
		wordsPositive=0
		wordsNegative=0
		wordDict={}
		for line in randomtraining:
			flag=''
			firstWord = True 
			words=line.split(' ')
			for word in words:
				if firstWord==False:
					x=word.split(':')[1]
					y=word.split(':')[0]
					#print(x,' ',y)
					if flag=='positive':
						wordsPositive+=int(x)
						if int(y) not in wordDict:
							wordDict[int(y)]=[int(x),0]
						else:
							a,b=wordDict[int(y)]
							wordDict[int(y)]=[a+int(x),b]
					if flag=='negative':
						wordsNegative+=int(x)
						if int(y) not in wordDict:
							wordDict[int(y)]=[0,int(x)]
						else:
							a,b=wordDict[int(y)]
							wordDict[int(y)]=[a,b+int(x)]
				if firstWord:
					if line.startswith('POSITIVE') or line.startswith('SPAM'):
						totalPositive+=1
						flag='positive'
					if line.startswith('NEGATIVE') or line.startswith('HAM'):
						totalNegative+=1
						flag='negative'
					firstWord=False	
		probPositive=totalPositive/totalSize
		probNegative=totalNegative/totalSize
		fileout.write(str(probPositive)+':'+str(probNegative))


		finalProb={}
		for i in wordDict:
			x,y=wordDict[i]
			finalProb[i]=[(x+1)/(wordsPositive+len(wordDict)),(y+1)/(wordsNegative+len(wordDict))]
			x,y=finalProb[i]
			fileout.write('\n'+str(i)+' '+str(x)+':'+str(y))



def main():
	trainingdata=readtrainingdata()
	calculateProbability(trainingdata)


if __name__ == "__main__": main()
