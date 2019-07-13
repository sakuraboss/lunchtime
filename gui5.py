from tkinter import *
from tkinter import ttk
import pandas as pd

#import csv to dataframe
df = pd.read_csv('lunch2.csv')

#Get unique values from .csv columns
def uniqueCuisine(dframe):
	global df_cuisine_unique
	global df_type_unique
	global cuisine_u_ct
	global type_u_ct
	
	#Get unique values from "Cuisine" column 
	df_cuisine_unique = df['Cuisine'].unique()
	#print(df_cuisine_unique)
	cuisine_u_ct = len(df_cuisine_unique)
	print(cuisine_u_ct)
	
	#Get Unique Items from "Specialty" column
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

#Get selected values.  Need to include "Fast Food" option
def selectValues():

	global pref
	global cvalue
	global tvalue
	global dvalue
	
	EmptyDF = pd.DataFrame(columns=['Name', 'Cuisine', 'Specialty', 'FF', 'DistMiles'])
	
	pref=cb.get()
	cvalue=[lb.get(cdx) for cdx in lb.curselection()]
	tvalue=[lb1.get(tdx) for tdx in lb1.curselection()]
	dvalue=[lb2.get(ddx) for ddx in lb2.curselection()]
	ff=var1.get()
	
	cuisine = df['Cuisine']	
	lenCuisine = (len(cvalue))
	
	#create another iteration for type of food	
	for x in range(y):	
	
		#create a container for items where df value is equal to list index value
		selectCuisine = cuisine==cvalue[x] 
		
		#create a new data frame with matched items
		cuisine0 = df[selectCuisine] 
		
		#merge dataframes
		EmptyDF = pd.concat([cuisine0, EmptyDF]) 
	
	print(EmptyDF.head(20)) #need to set to.....
			
	#Distance should be int so selection is <= value
	
	if pref == '':
		print("Preference required")
		
	elif pref == "I want" and ff == 1: #AND Fast Food is true, print all where distance is <= value
		#where distance is >=
			print("I Like Fast Food")
		#Build logic for selection
	
	elif pref == "I want" and ff == 0:  #AND Fast Food is false, print all where distance is <=value
		#where distance is >=
			print("No fast food for me")
		
	elif pref == "I don't want" and ff == 1:  #AND Fast Food is true, print inverse where distance is <= value
		#where distance is >=
			print("I don't want any of this but I want fast food")
		
	elif pref == "I don't want" and ff == 0:
		#where distance is >=
			print("I don't want any of this and I don't want fast food either")
			
			
#Clear items		
def resetValues():
	cb.set('')
	lb.selection_clear(0, END)
	lb1.selection_clear(0, END)
	lb2.selection_clear(0, END)
	ckb.deselect()

#Build GUI	
def buildGUI(cuisine, cuisinect, type, typect):
#Create a GUI Window
	m = Tk()
	global m
	global cb
	global lb
	global lb1
	global lb2
	global ckb
	global var1
	
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
	
	#Insert unique "Cuisine" Items.  Would like to change to have a max of 10 with scrollbar
	lb = Listbox(m, height=cuisinect, selectmode=MULTIPLE, exportselection=0)  #selectmode=MULTIPLE
	for item in cuisine:
		lb.insert(END, item)

	#Insert unique "Specialty" Items.  Would like to change to have a max of 10 with scrollbar
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
	
	#Would like the "Preference" selection to be mandatory.  If not, show error message
	btn = Button(m, text='Submit', width=12, bg = "green", command=selectValues)
	btn1 = Button(m, text='Clear', width=12, command=resetValues) #command=printName

	
	#GUI Layout.  Need scrollbars on listboxes
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
	btn.grid(row=5, column=3, sticky=E + S)   
	btn1.grid(row=5, column=2, sticky=E + S)
	#scrollbar.grid(row=2, column=1, sticky=N+S)

	m.mainloop()
	
uniqueCuisine(df)
buildGUI(df_cuisine_unique, cuisine_u_ct, df_type_unique, type_u_ct)
