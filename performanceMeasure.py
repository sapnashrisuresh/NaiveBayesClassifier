#Used to measure precision, recall and F-score to measure the performance of each model. 
#The values are displayed as % for better comparison between models.

#To run the script, provide the reference results and the output of the current model, followed by an option (1:Sentiment Analysis, 2:SPAM filtering,
#3:SVM, 4:MegaM)

#python3 performanceMeasure.py sentiment.reference25.out sentiment25.nb.out 1

import sys

reference=sys.argv[1]
output=sys.argv[2]
option=sys.argv[3]

with open(reference,'r') as ref, open(output,'r') as op:
	reflist=[]
	oplist=[]
	for line in ref.readlines():
		reflist.append(line)
	for line in op.readlines():
		oplist.append(line)

	if(option=='1'):
		TP=0
		FN=0
		FP=0
		i=0
		while i<len(reflist):
			if(oplist[i]=='POSITIVE\n' and reflist[i]!='POSITIVE\n'):
				FP+=1
			if(reflist[i]=='POSITIVE\n' and oplist[i]!='POSITIVE\n'):
				FN+=1
			if(reflist[i]=='POSITIVE\n' and oplist[i]=='POSITIVE\n'):
				TP+=1
			i+=1	

		precision=TP/(TP+FP)  
		recall=TP/(TP+FN)
		fscore=(2*precision*recall)/(precision+recall)
		print("Values for Sentiment Data (POSITIVE):")
		print('Precision =',precision*100,' Recall =',recall*100,' F-Score=',fscore*100)

		TP=0
		FN=0
		FP=0
		i=0

		while i<len(reflist):
			if(oplist[i]=='NEGATIVE\n' and reflist[i]!='NEGATIVE\n'):
				FP+=1
			if(reflist[i]=='NEGATIVE\n' and oplist[i]!='NEGATIVE\n'):
				FN+=1
			if(reflist[i]=='NEGATIVE\n' and oplist[i]=='NEGATIVE\n'):
				TP+=1
			i+=1	

		precision=TP/(TP+FP)
		recall=TP/(TP+FN)
		fscore=(2*precision*recall)/(precision+recall)
		print("Values for Sentiment Data (NEGATIVE):")
		print('Precision =',precision*100,' Recall =',recall*100,' F-Score=',fscore*100)

	if(option=='2'):
		TP=0
		FN=0
		FP=0
		i=0
		while i<len(reflist):
			if(oplist[i]=='SPAM\n' and reflist[i]!='SPAM\n'):
				FP+=1
			if(reflist[i]=='SPAM\n' and oplist[i]!='SPAM\n'):
				FN+=1
			if(reflist[i]=='SPAM\n' and oplist[i]=='SPAM\n'):
				TP+=1
			i+=1	

		precision=TP/(TP+FP)  
		recall=TP/(TP+FN)
		fscore=(2*precision*recall)/(precision+recall)
		print("Values for Spam Data (SPAM):")
		print('Precision =',precision*100,' Recall =',recall*100,' F-Score=',fscore*100)

		TP=0
		FN=0
		FP=0
		i=0

		while i<len(reflist):
			if(oplist[i]=='HAM\n' and reflist[i]!='HAM\n'):
				FP+=1
			if(reflist[i]=='HAM\n' and oplist[i]!='HAM\n'):
				FN+=1
			if(reflist[i]=='HAM\n' and oplist[i]=='HAM\n'):
				TP+=1
			i+=1	

		precision=TP/(TP+FP)
		recall=TP/(TP+FN)
		fscore=(2*precision*recall)/(precision+recall)
		print("Values for Spam Data (HAM):")
		print('Precision =',precision*100,' Recall =',recall*100,' F-Score=',fscore*100)

	if(option=='3'):
		TP=0
		FN=0
		FP=0
		i=0
		while i<len(reflist):
			if(float(oplist[i])>0 and float(reflist[i])<0):
				FP+=1
			if(float(reflist[i])>0 and float(oplist[i])<0):
				FN+=1
			if(float(reflist[i])>0 and float(oplist[i])>0):
				TP+=1
			i+=1	

		precision=TP/(TP+FP)  
		recall=TP/(TP+FN)
		fscore=(2*precision*recall)/(precision+recall)
		print("Values for SVM (POSITIVE/SPAM):")
		print('Precision =',precision*100,' Recall =',recall*100,' F-Score=',fscore*100)

		TP=0
		FN=0
		FP=0
		i=0

		while i<len(reflist):
			if(float(oplist[i])<0 and float(reflist[i])>0):
				FP+=1
			if(float(reflist[i])<0 and float(oplist[i])>0):
				FN+=1
			if(float(reflist[i])<0 and float(oplist[i])<0):
				TP+=1
			i+=1	

		precision=TP/(TP+FP)
		recall=TP/(TP+FN)
		fscore=(2*precision*recall)/(precision+recall)
		print("Values for SVM (NEGATIVE/HAM):")
		print('Precision =',precision*100,' Recall =',recall*100,' F-Score=',fscore*100)

	if(option=='4'):
		TP=0
		FN=0
		FP=0
		i=0
		for line in oplist:
			if(int(line[0])==1 and int(reflist[i])==0):
				FP+=1
			if(int(reflist[i])==1 and int(line[0])==0):
				FN+=1
			if(int(reflist[i])==1 and int(line[0])==1):
				TP+=1
			i+=1	

		precision=TP/(TP+FP)  
		recall=TP/(TP+FN)
		fscore=(2*precision*recall)/(precision+recall)
		print("Values for MegaM (POSITIVE/SPAM):")
		print('Precision =',precision*100,' Recall =',recall*100,' F-Score=',fscore*100)

		TP=0
		FN=0
		FP=0
		i=0

		for line in oplist:
			if(int(line[0])==0 and int(reflist[i])==1):
				FP+=1
			if(int(reflist[i])==0 and int(line[0])==1):
				FN+=1
			if(int(reflist[i])==0 and int(line[0])==0):
				TP+=1
			i+=1

		precision=TP/(TP+FP)
		recall=TP/(TP+FN)
		fscore=(2*precision*recall)/(precision+recall)
		print("Values for MegaM (NEGATIVE/HAM):")
		print('Precision =',precision*100,' Recall =',recall*100,' F-Score=',fscore*100)