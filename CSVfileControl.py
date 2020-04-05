"""
Name: Liam Hovey
SN: 040774944
Exercise 3
"""

import csv

import rowOBJ

"""open the file of the name 13100262"""
filename = "13100262.csv"
"""the names of all the fields"""
fieldnames = ['REF_DATE', 'GEO', 'DGUID', 'Sex', 'Age group', 'Student response', 'UOM', 'UOM_ID', 'SCALAR_FACTOR',
              'SCALAR_ID', 'VECTOR', 'COORDINATE', 'VALUE', 'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS']
# the array
arrayOfRows = []


# takes all rows from the csv and places them in the array
def load_all_from_csv():
    print("REF_DATE, GEO, DGUID, Sex, Age group, Student response, UOM, UOM_ID, SCALAR_FACTOR, SCALAR_ID, VECTOR, "
          "COORDINATE, VALUE, STATUS, SYMBOL, TERMINATED, DECIMALS")
    # clear the list
    del arrayOfRows[:]
    with open(filename, newline='') as csv_file:
        """create a reader object out of the csv file"""
        csv_reader = csv.DictReader(csv_file)
        rowCount = 0
        """append each of the rows onto the array so that we have an array of our custom object"""
        for row in csv_reader:
            # don't place the header in the array
            rowCount += 1
            # append to the array a row object with the values found
            arrayOfRows.append(
                rowOBJ.RowObj(row['REF_DATE'], row['GEO'], row['DGUID'], row['Sex'], row['Age group'],
                              row['Student response'], row['UOM'], row['UOM_ID'], row['SCALAR_FACTOR'],
                              row['SCALAR_ID'],
                              row['VECTOR'], row['COORDINATE'], row['VALUE'], row['STATUS'], row['SYMBOL'],
                              row['TERMINATED'], row['DECIMALS']
                              ))

    print("this program made by Liam Hovey SN 040774944")


def get_array_of_column(column):
    arrayOfColumn = []
    for x in arrayOfRows:
        if column == 'REF_DATE':
            arrayOfColumn.append(x.REF_DATE)
        if column == 'GEO':
            arrayOfColumn.append(x.GEO)
        if column == 'DGUID':
            arrayOfColumn.append(x.DGUID)
        if column == 'Sex':
            arrayOfColumn.append(x.SEX)
        if column == 'AGE':
            arrayOfColumn.append(x.AGE)
        if column == 'STUDENT':
            arrayOfColumn.append(x.STUDENT)
        if column == 'UOM':
            arrayOfColumn.append(x.UOM)
        if column == 'UOM_ID':
            arrayOfColumn.append(x.UOM_ID)
        if column == 'SCALAR_FACTOR':
            arrayOfColumn.append(x.SCALAR_FACTOR)
        if column == 'SCALAR_ID':
            arrayOfColumn.append(x.SCALAR_ID)
        if column == 'VECTOR':
            arrayOfColumn.append(x.VECTOR)
        if column == 'COORDINATE':
            arrayOfColumn.append(x.COORDINATE)
        if column == 'VALUE':
            arrayOfColumn.append(x.VALUE)
        if column == 'STATUS':
            arrayOfColumn.append(x.STATUS)
        if column == 'SYMBOL':
            arrayOfColumn.append(x.SYMBOL)
        if column == 'TERMINATED':
            arrayOfColumn.append(x.TERMINATED)
        if column == 'DECIMALS':
            arrayOfColumn.append(x.DECIMALS)
    return arrayOfColumn


# gets all unique values in the array at a given column
def get_unique_values(column):
    list_of_unique_values = []
    arrayOfColumn = get_array_of_column(column)
    for x in arrayOfColumn:
        if x not in list_of_unique_values:
            list_of_unique_values.append(x)
    return list_of_unique_values


def number_of_value_in_set(column, value_number):
    i = 0
    full_set = get_array_of_column(column)
    unique_values = get_unique_values(column)
    for x in full_set:
        if x == unique_values[value_number]:
            i = i + 1
    return i


# creates the string functions as a chart
def make_chart_string(column):
    listofcolumn = get_unique_values(column)
    bar_graph = ""
    for i in range(len(listofcolumn)):
        bar_graph += listofcolumn[i] + " " + str(round(get_percentage(column, i), 2)) + "% \t\t" + get_percentage_bar(
            column, i) + "\n"
    return bar_graph


def get_percentage(column, value_number):
    return 100 * number_of_value_in_set(column, value_number) / len(get_array_of_column(column))


def get_percentage_bar(column, value_number):
    s = ""
    i = 0
    while i < get_percentage(column, value_number):
        s += "*"
        i += 2
    return s


# read the first x lines of the array
def read_first_x(x):
    i = 0
    """loop through the array that wee mad and use the str function to print them out"""
    while i < x:
        print(arrayOfRows[i])
        i += 1
    print("this program made by Liam Hovey SN 040774944")


# deletes the x'th row
def delete_row(x):
    del arrayOfRows[x]
    print("this program made by Liam Hovey SN 040774944")


# read all the rows in the array list
def read_all():
    """loop through the array that wee mad and use the str function to print them out"""
    for i in range(len(arrayOfRows)):
        print(arrayOfRows[i])
    print("this program made by Liam Hovey SN 040774944")


# read raw from file
def read_raw():
    reader = csv.DictReader(open(filename))
    for raw in reader:
        print(raw)
    print("this program made by Liam Hovey SN 040774944")


# read the x'th row of the array
def read_x(x):
    print(arrayOfRows[x])
    print("this program made by Liam Hovey SN 040774944")


def persist():
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL, delimiter=',')
        # loop through array
        for i in range(len(arrayOfRows)):
            # write eliment of array to to csv file
            csv_writer.writerow(
                [arrayOfRows[i].REF_DATE, arrayOfRows[i].GEO, arrayOfRows[i].DGUID, arrayOfRows[i].SEX,
                 arrayOfRows[i].AGE, arrayOfRows[i].STUDENT, arrayOfRows[i].UOM, arrayOfRows[i].UOM_ID,
                 arrayOfRows[i].SCALAR_FACTOR, arrayOfRows[i].SCALAR_ID, arrayOfRows[i].VECTOR,
                 arrayOfRows[i].COORDINATE, arrayOfRows[i].VALUE, arrayOfRows[i].STATUS, arrayOfRows[i].SYMBOL,
                 arrayOfRows[i].TERMINATED, arrayOfRows[i].DECIMALS])
    print("this program made by Liam Hovey SN 040774944")


# adds a row object to the array
def add(a, b, c, d, e, f, g, h, i, j, k, ll, m, n, o, p, q):
    arrayOfRows.append(rowOBJ.RowObj(a, b, c, d, e, f, g, h, i, j, k, ll, m, n, o, p, q))
    print("this program made by Liam Hovey SN 040774944")


# sorts on a given index of a attribute
def sort_on(y):
    if y == 1:
        arrayOfRows.sort(key=lambda x: x.REF_DATE)
    if y == 2:
        arrayOfRows.sort(key=lambda x: x.GEO)
    if y == 3:
        arrayOfRows.sort(key=lambda x: x.DGUID)
    if y == 4:
        arrayOfRows.sort(key=lambda x: x.SEX)
    if y == 5:
        arrayOfRows.sort(key=lambda x: x.AGE)
    if y == 6:
        arrayOfRows.sort(key=lambda x: x.STUDENT)
    if y == 7:
        arrayOfRows.sort(key=lambda x: x.UOM)
    if y == 8:
        arrayOfRows.sort(key=lambda x: x.UOM_ID)
    if y == 9:
        arrayOfRows.sort(key=lambda x: x.SCALAR_FACTOR)
    if y == 10:
        arrayOfRows.sort(key=lambda x: x.SCALAR_ID)
    if y == 11:
        arrayOfRows.sort(key=lambda x: x.VECTOR)
    if y == 12:
        arrayOfRows.sort(key=lambda x: x.COORDINATE)
    if y == 13:
        arrayOfRows.sort(key=lambda x: x.VALUE)
    if y == 14:
        arrayOfRows.sort(key=lambda x: x.STATUS)
    if y == 15:
        arrayOfRows.sort(key=lambda x: x.SYMBOL)
    if y == 16:
        arrayOfRows.sort(key=lambda x: x.TERMINATED)
    if y == 16:
        arrayOfRows.sort(key=lambda x: x.DECIMALS)


# takes the row and column that you want to change
# and change it to value
def update(row, column, value):
    if column == 1:
        arrayOfRows[row].REF_DATE = value
    if column == 2:
        arrayOfRows[row].GEO = value
    if column == 3:
        arrayOfRows[row].DGUID = value
    if column == 4:
        arrayOfRows[row].SEX = value
    if column == 5:
        arrayOfRows[row].AGE = value
    if column == 6:
        arrayOfRows[row].STUDENT = value
    if column == 7:
        arrayOfRows[row].UOM = value
    if column == 8:
        arrayOfRows[row].UOM_ID = value
    if column == 9:
        arrayOfRows[row].SCALAR_FACTOR = value
    if column == 10:
        arrayOfRows[row].SCALAR_ID = value
    if column == 11:
        arrayOfRows[row].VECTOR = value
    if column == 12:
        arrayOfRows[row].COORDINATE = value
    if column == 13:
        arrayOfRows[row].VALUE = value
    if column == 14:
        arrayOfRows[row].STATUS = value
    if column == 15:
        arrayOfRows[row].SYMBOL = value
    if column == 16:
        arrayOfRows[row].TERMINATED = value
    if column == 17:
        arrayOfRows[row].DECIMALS = value
    print("this program made by Liam Hovey SN 040774944")
