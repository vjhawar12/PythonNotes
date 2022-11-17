def text(): 
	# opening text files
	fileName = "python.txt"

	with open(fileName) as f: 
		for line in f: 
			print(line, end="")

def csv():         
	# opening csv files 
	import csv 

	fileName = "csvone.csv"
	with open(fileName) as f: 
		reader = csv.reader(f)
		lines = 0
		for row in reader:
			print(row)
			lines += 1


def json():
    # opening json files
    import json
    fileName = "json.json"
    file = open(fileName, "r")
    
    # load method returns a dictionary
    dic = json.load(file)
    for k in dic.keys(): 
        print(k)
    file.close()    
    
    # loads method loads a string
    string = json.loads(file.read())
    print(string)
    file.close()

json() 
    