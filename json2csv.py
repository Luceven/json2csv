# Author: Kate Zeng
# 07/24/2020
import json
import csv
import glob

def main():
	# get all json files
	filenames = glob.glob("*.json")
	# iterate through all filenames
	for name in filenames:
		with open(name) as json_file:
			data = json.load(json_file)

		# convert file
		csv_name = name[:-5] + '.csv'
		output = open(csv_name, 'w')
		csvwriter = csv.writer(output)
		count = 0
		for dat in data:
			if count == 0:
				header = dat.keys()
				csvwriter.writerow(header)
				count += 1
			csvwriter.writerow(dat.values())
		output.close()

if __name__ == "__main__":
	main()