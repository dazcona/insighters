import csv

def createCSV():
	fields=['second', 'result']
	with open(r'results.csv', 'a') as f:
	    writer = csv.writer(f)
	    writer.writerow(fields)
def editCSV(second,result):
	fields=[second, result]
	with open(r'results.csv', 'a') as f:
	    writer = csv.writer(f)
	    writer.writerow(fields)
