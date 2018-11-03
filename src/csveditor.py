import csv

def create_csv():
	fields=['second', 'result']
	with open(r'results.csv', 'w') as f:
	    writer = csv.writer(f)
	    writer.writerow(fields)

def edit_csv(second,result):
	fields=[second, result]
	with open(r'results.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow(fields)
