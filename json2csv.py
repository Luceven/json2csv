# Author: Kate Zeng
# 07/24/2020
import json
import csv
import glob
from tkinter import *
from tkinter.filedialog import askdirectory

def onEnterDir(dropdown, var):
    path = askdirectory()
    if not path:
        return
    filenames = glob.glob("*.json")
    dropdown.configure(state='normal')  # Enable drop down
    menu = dropdown['menu']

    # Clear the menu
    menu.delete(0, 'end')
    for name in filenames:
        # Add menu items
        menu.add_command(label=name, command=lambda name=name: var.set(name))
        # OR menu.add_command(label=name, command=partial(var.set, name))

def main():
	# create user interface using Tkinter
	app = Tk()
	app.title("json2csv v1.0")
	app.geometry('280x150')
	# create a Tkinter variable
	tkvar = StringVar(app)

	dropdown = OptionMenu(app, tkvar, "Select JSON...")
	Label(app, text="Please choose json file").grid(row=1, column=1)
	dropdown.grid(row=2, column=2)
	dropdown.configure(state='disabled')

	b = Button(app, text='Change Directory', command=lambda: onEnterDir(dropdown, tkvar))
	b.grid(row=2, column=1)

	def convert_json(*args):
		global name
		# the the name that selected by user
		name = str(tkvar.get())

		with open(name) as json_file:
			data = json.load(json_file)

		# convert file
		csv_name = name[:-5] + '.csv'
		output = open(csv_name, 'w', newline='', encoding='utf-8')
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
	b1.grid(row=10, column=1)
	b2 = Button(app, text='Close', command=app.quit)
	b2.grid(row=10, column=2)

	labelTest = Label(text="", fg='red')
	labelTest.grid(row=4, column=1)

	app.mainloop()

if __name__ == "__main__":
	main()