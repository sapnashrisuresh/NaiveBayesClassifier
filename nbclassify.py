import sys,math

modelfile=sys.argv[1]
testfile=sys.argv[2]

def prior():
	with open(modelfile,'r') as model:
		firstline=True
		posDict={}
		negDict={}
		if(str(modelfile).startswith('spam')):
			flag=1
		else:
			flag=0
		for line in model.readlines():
			if(firstline==False):
				words=line.split()
				key=int(words[0])
				values=words[1].split(':')
				posDict[key]=float(values[0])
				negDict[key]=float(values[1])
				#print(key,posDict[key],negDict[key])
			else:
				words=line.split(':')
				posPrior=math.log(float(words[0]))
				negPrior=math.log(float(words[1]))
				firstline=False
		#print(posPrior,' ',negPrior)
		return(posPrior,negPrior,posDict,negDict,flag)

def classify(posPrior,negPrior,posDict,negDict,flag):
	with open(testfile,'r') as test:
		for line in test.readlines():
			posPosterior=posPrior
			negPosterior=negPrior
			firstWord=True
			words=line.split()
			for word in words:
				if(firstWord==False):
					feature=word.split(':')
					key=int(feature[0])
					frequency=int(feature[1])
					pos=posDict.get(key,0)
					neg=negDict.get(key,0)
					if(pos!=0):
						posPosterior+=(frequency*math.log(pos))
					if(neg!=0):
						negPosterior+=(frequency*math.log(neg))
				else:
					firstWord=False
			if(flag==1):
				if(posPosterior>=negPosterior):
					sys.stdout.write('SPAM\n')
				else:
					sys.stdout.write('HAM\n')
			else:
				if(posPosterior>=negPosterior):
					sys.stdout.write('POSITIVE\n')
				else:
					sys.stdout.write('NEGATIVE\n')

def main():
	posPrior,negPrior,posDict,negDict,flag=prior()
	classify(posPrior,negPrior,posDict,negDict,flag)



if __name__ == "__main__": main()