# Author: Kate Zeng
# 07/24/2020
import json
import csv
import glob
from tkinter import *

def main():
	# get all json files
	filenames = glob.glob("*.json")

	# create user interface using Tkinter
	app = Tk()
	app.title("json2csv v1.0")
	app.geometry('220x150')
	# create a Tkinter variable
	tkvar = StringVar(app)
	# options copied from glob list
	choices = filenames
	# set the default option
	tkvar.set(choices[0])

	dropdown = OptionMenu(app, tkvar, *choices)
	Label(app, text="Please choose json file").grid(row=2, column=2)
	dropdown.grid(row=3, column=2)

	def convert_json(*args):
		global name
		# the the name that selected by user
		name = str(tkvar.get())

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

		labelTest.configure(text="{} converted!".format(name))

	b1 = Button(app, text='Convert', command=convert_json)
	b1.grid(row=3, column=3)
	b2 = Button(app, text='Close', command=app.quit)
	b2.grid(row=6, column=2)

	labelTest = Label(text="", fg='red')
	labelTest.grid(row=8, column=2)

	# on change dropdown value
	#def change_dropdown(*args):
		#labelTest.configure(text="{} converted!".format(tkvar.get()))

	# link function to change dropdown
	#tkvar.trace('w', change_dropdown)
	app.mainloop()

if __name__ == "__main__":
	main()