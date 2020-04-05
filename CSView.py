"""
Name: Liam Hovey
SN: 040774944
Assignment 3
"""
import tkinter.scrolledtext

import self as self

import CSVfileControl
from tkinter import *
from tkinter import ttk

CSVfileControl.load_all_from_csv()
window = Tk()
window.title("CSV File Reader")
window.geometry('1200x650')
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='manage')
tab_control.add(tab2, text='insert')
tab_control.add(tab3, text='visualize')


def clicked_get_all():
    txt.delete(1.0, END)
    for index in range(len(CSVfileControl.arrayOfRows)):
        txt.insert(INSERT, CSVfileControl.arrayOfRows[index])
        txt.insert(INSERT, "\n")


def del_index():
    CSVfileControl.delete_row(int(index_to_del.get()))


def update():
    CSVfileControl.update(int(row_to_update.get()), int(column_update.get()), value_update.get())


def sort_on():
    CSVfileControl.sort_on(int(sort_on.get()))


def persist():
    CSVfileControl.persist()


def get_from_csv():
    CSVfileControl.load_all_from_csv()


def add():
    CSVfileControl.add(REF_DATE_edit.get(), GEO_edit.get(), DGUID_edit.get(), Sex_edit.get(), Age_group_edit.get(),
                       Student_response_edit.get(), UOM_edit.get(), UOM_ID_edit.get(), SCALAR_FACTOR_edit.get(),
                       SCALAR_ID_edit.get(),
                       VECTOR_edit.get(), COORDINATE_edit.get(), VALUE_edit.get(), STATUS_edit.get(), SYMBOL_edit.get(),
                       TERMINATED_edit.get(), DECIMALS_edit.get())


def visualise_graph(i):
    txt2.delete(1.0, END)
    txt2.insert(INSERT, CSVfileControl.make_chart_string(i))


instructions = Label(tab1, text="Liam Hovey 040774944")
instructions.grid(column=0, row=0)
getAllBtn = Button(tab1, text="Get All", command=clicked_get_all)
getAllBtn.grid(column=1, row=0)
delBtn = Button(tab1, text="delete", command=del_index)
delBtn.grid(column=1, row=1)
updateBtn = Button(tab1, text="update", command=update)
updateBtn.grid(column=1, row=2)
sortBtn = Button(tab1, text="sort", command=sort_on)
sortBtn.grid(column=1, row=3)
persistBtn = Button(tab1, text="persist", command=persist)
persistBtn.grid(column=1, row=4)
retreveBtn = Button(tab1, text="retreve", command=get_from_csv)
retreveBtn.grid(column=1, row=5)
index_to_del = Entry(tab1, width=5)
row_to_update = Entry(tab1, width=5)
column_update = Entry(tab1, width=5)
value_update = Entry(tab1, width=5)
sort_on = Entry(tab1, width=5)
row_to_update.grid(column=2, row=2)
column_update.grid(column=3, row=2)
value_update.grid(column=4, row=2)
index_to_del.grid(column=2, row=1)
sort_on.grid(column=2, row=3)
txt = tkinter.scrolledtext.ScrolledText(tab1, width=120, height=30)
txt.grid(column=0, row=1)
txt2 = tkinter.scrolledtext.ScrolledText(tab3, width=120, height=30)
txt2.grid(column=0, row=1, columnspan=17)

Btn1 = Button(tab3, text="REF_DATE", command=lambda: visualise_graph('REF_DATE'))
Btn1.grid(column=0, row=0)
Btn2 = Button(tab3, text="GEO", command=lambda: visualise_graph('GEO'))
Btn2.grid(column=1, row=0)
Btn3 = Button(tab3, text="DGUID", command=lambda: visualise_graph('DGUID'))
Btn3.grid(column=2, row=0)
Btn4 = Button(tab3, text="Sex", command=lambda: visualise_graph('Sex'))
Btn4.grid(column=3, row=0)
Btn5 = Button(tab3, text="AGE", command=lambda: visualise_graph('AGE'))
Btn5.grid(column=4, row=0)
Btn6 = Button(tab3, text="STUDENT", command=lambda: visualise_graph('STUDENT'))
Btn6.grid(column=5, row=0)
Btn7 = Button(tab3, text="UOM", command=lambda: visualise_graph('UOM'))
Btn7.grid(column=6, row=0)
Btn8 = Button(tab3, text="UOM_ID", command=lambda: visualise_graph('UOM_ID'))
Btn8.grid(column=7, row=0)
Btn9 = Button(tab3, text="SCALAR_FACTOR", command=lambda: visualise_graph('SCALAR_FACTOR'))
Btn9.grid(column=8, row=0)
Btn10 = Button(tab3, text="SCALAR_ID", command=lambda: visualise_graph('SCALAR_ID'))
Btn10.grid(column=9, row=0)
Btn11 = Button(tab3, text="VECTOR", command=lambda: visualise_graph('VECTOR'))
Btn11.grid(column=10, row=0)
Btn12 = Button(tab3, text="COORDINATE", command=lambda: visualise_graph('COORDINATE'))
Btn12.grid(column=11, row=0)
Btn13 = Button(tab3, text="VALUE", command=lambda: visualise_graph('VALUE'))
Btn13.grid(column=12, row=0)
Btn14 = Button(tab3, text="STATUS", command=lambda: visualise_graph('STATUS'))
Btn14.grid(column=13, row=0)
Btn15 = Button(tab3, text="SYMBOL", command=lambda: visualise_graph('SYMBOL'))
Btn15.grid(column=14, row=0)
Btn16 = Button(tab3, text="TERMINATED", command=lambda: visualise_graph("TERMINATED"))
Btn16.grid(column=15, row=0)
Btn17 = Button(tab3, text="DECIMALS", command=lambda: visualise_graph("DECIMALS"))
Btn17.grid(column=16, row=0)

REF_DATE = Label(tab2, text="REF_DATE")
GEO = Label(tab2, text="GEO")
DGUID = Label(tab2, text="DGUID")
Sex = Label(tab2, text="Sex")
Age_group = Label(tab2, text="Age_group")
Student_response = Label(tab2, text="Student_response")
UOM = Label(tab2, text="UOM")
UOM_ID = Label(tab2, text="UOM_ID")
SCALAR_FACTOR = Label(tab2, text="SCALAR_FACTOR")
SCALAR_ID = Label(tab2, text="SCALAR_ID")
VECTOR = Label(tab2, text="VECTOR")
COORDINATE = Label(tab2, text="COORDINATE")
VALUE = Label(tab2, text="VALUE")
STATUS = Label(tab2, text="STATUS")
SYMBOL = Label(tab2, text="SYMBOL")
TERMINATED = Label(tab2, text="TERMINATED")
DECIMALS = Label(tab2, text="DECIMALS")

REF_DATE.grid(column=0, row=0)
GEO.grid(column=1, row=0)
DGUID.grid(column=2, row=0)
Sex.grid(column=3, row=0)
Age_group.grid(column=4, row=0)
Student_response.grid(column=5, row=0)
UOM.grid(column=6, row=0)
UOM_ID.grid(column=7, row=0)
SCALAR_FACTOR.grid(column=8, row=0)
SCALAR_ID.grid(column=9, row=0)
VECTOR.grid(column=10, row=0)
COORDINATE.grid(column=11, row=0)
VALUE.grid(column=12, row=0)
STATUS.grid(column=13, row=0)
SYMBOL.grid(column=14, row=0)
TERMINATED.grid(column=15, row=0)
DECIMALS.grid(column=16, row=0)

REF_DATE_edit = Entry(tab2, width=10)
GEO_edit = Entry(tab2, width=10)
DGUID_edit = Entry(tab2, width=10)
Sex_edit = Entry(tab2, width=10)
Age_group_edit = Entry(tab2, width=10)
Student_response_edit = Entry(tab2, width=10)
UOM_edit = Entry(tab2, width=10)
UOM_ID_edit = Entry(tab2, width=10)
SCALAR_FACTOR_edit = Entry(tab2, width=10)
SCALAR_ID_edit = Entry(tab2, width=10)
VECTOR_edit = Entry(tab2, width=10)
COORDINATE_edit = Entry(tab2, width=10)
VALUE_edit = Entry(tab2, width=10)
STATUS_edit = Entry(tab2, width=10)
SYMBOL_edit = Entry(tab2, width=10)
TERMINATED_edit = Entry(tab2, width=10)
DECIMALS_edit = Entry(tab2, width=10)
REF_DATE_edit.grid(column=0, row=1)
GEO_edit.grid(column=1, row=1)
DGUID_edit.grid(column=2, row=1)
Sex_edit.grid(column=3, row=1)
Age_group_edit.grid(column=4, row=1)
Student_response_edit.grid(column=5, row=1)
UOM_edit.grid(column=6, row=1)
UOM_ID_edit.grid(column=7, row=1)
SCALAR_FACTOR_edit.grid(column=8, row=1)
SCALAR_ID_edit.grid(column=9, row=1)
VECTOR_edit.grid(column=10, row=1)
COORDINATE_edit.grid(column=11, row=1)
VALUE_edit.grid(column=12, row=1)
STATUS_edit.grid(column=13, row=1)
SYMBOL_edit.grid(column=14, row=1)
TERMINATED_edit.grid(column=15, row=1)
DECIMALS_edit.grid(column=16, row=1)
addBtn = Button(tab2, text="add", command=add)
addBtn.grid(column=0, row=2)

tab_control.pack(expand=1, fill='both')

window.mainloop()
