#Scroll bars on list boxes and limit display of 10 items
#Match logic
#Command calls

from tkinter import *
from tkinter import ttk
import pandas as pd

df = pd.read_csv('lunch2.csv')

def uniqueCuisine(dframe):
	global df_cuisine_unique
	global df_type_unique
	global cuisine_u_ct
	global type_u_ct

	df_cuisine_unique = df['Cuisine'].unique()
	#print(df_cuisine_unique)
	cuisine_u_ct = len(df_cuisine_unique)
	print(cuisine_u_ct)
	
	
	df_type_unique = df['Specialty'].unique()
	#print(df_type_unique)
	type_u_ct = len(df_type_unique)
	print(type_u_ct)
	
'''
def selectItems()
	cuisine = input("What kind of cuisine would you like?")
	food = input("What type of food do you want?")
	type = input("Do you want fast food?")

	is_cuisine = df['Cuisine']==cuisine
	is_food = df['Specialty']==food
	is_type = df['Type']==type

	df_cuisine = df[is_cuisine]
	df_food = df[is_food]
	df_type = df[is_type]
'''

'''def testPass(cuisine, type):
	print("Test Passed")
	print(cuisine)	
	print(type)

uniqueCuisine(df)
testPass(df_cuisine_unique, df_type_unique)'''

def selectValues():

		global pref
		global cvalue
		global tvalue
		global dvalue
		
		#print("Hello!")
		pref=cb.get()
		cvalue=[lb.get(cdx) for cdx in lb.curselection()]
		tvalue=[lb1.get(tdx) for tdx in lb1.curselection()]
		dvalue=[lb2.get(ddx) for ddx in lb2.curselection()]
			
	
		print(pref)
		ctype=type(cvalue)
		print(ctype)
		print(cvalue)
		print(tvalue)
		print(dvalue)
		
		if pref == "I want":
			print("Like")
			
		elif pref == "I don't want":
			print("No Like")
			
		
def resetValues():
	cb.set('')
	lb.selection_clear(0, END)
	lb1.selection_clear(0, END)
	lb2.selection_clear(0, END)
	ckb.deselect()


	
		
		

def buildGUI(cuisine, cuisinect, type, typect):
#Create a GUI Window
	m = Tk()
	global cb
	global lb
	global lb1
	global lb2
	global ckb
	
	#Actions for Events
	
	#Window title
	m.title("Important Task of the Day")

	#Create Objects in Window
	lbl0 = Label(m, text="What's for Lunch?", font=("Calibri", 22))	
	lblCuisine = Label(m, text="Cuisine")
	lblType	= Label(m, text="Type")		
	lblDist = Label(m, text="Distance")
	lblPref = Label(m, text = "*Preference")
	lblReq = Label(m, text="*Required Field")

	cb = ttk.Combobox(m, state="readonly", values = ["I want", "I don't want"])
	#entry_1 = Entry(m)
	
	
	lb = Listbox(m, height=cuisinect, selectmode=MULTIPLE, exportselection=0)  #selectmode=MULTIPLE
	for item in cuisine:
		lb.insert(END, item)


	lb1 = Listbox(m, height=typect, selectmode=MULTIPLE, exportselection=0) #selectmode=MULTIPLE
	for item in type:
		lb1.insert(END,item)
	
	lb2 = Listbox(m, height = 4)
	lb2.insert(1, "1 Mile")
	lb2.insert(2, "5 Miles")
	lb2.insert(3, "10 Miles")
	lb2.insert(4, "15 Miles")

	var1 = IntVar()
	ckb = Checkbutton(m, text = "Fast Food?", variable = var1)

	btn = Button(m, text='Submit', width=12, bg = "green", command=selectValues)
	btn1 = Button(m, text='Clear', width=12, command=resetValues) #command=printName

	#default column = 0
	lbl0.grid(columnspan = 4) #Set columnspan to max number of columns?
	#lbl.grid(row=2, column = 0)
	lblCuisine.grid(row = 1, column = 1)
	lblType.grid(row = 1, column = 2)
	lblDist.grid(row = 1, column =3)
	lblPref.grid(row = 1, column = 0)
	lblReq.grid(row = 5, column = 0, sticky=W)
	cb.grid(row = 2, column = 0, sticky=N)
	ckb.grid(row=4, column=3)
	lb.grid(row = 2, column = 1, sticky=N)
	lb1.grid(row = 2, column= 2, sticky=N)
	lb2.grid(row = 2, column = 3, sticky=N)
	btn.grid(row=5, column=3, sticky=E + S)    #Set columnspan to max number of columns?
	btn1.grid(row=5, column=2, sticky=E + S)
	#scrollbar.grid(row=2, column=1, sticky=N+S)

	m.mainloop()
uniqueCuisine(df)
buildGUI(df_cuisine_unique, cuisine_u_ct, df_type_unique, type_u_ct)