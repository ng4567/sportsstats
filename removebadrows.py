#author = Nikhil Gopal
#this script is written because sometimes certain players had more than one run values assigned to them, or because they had no value
#which screwed up my data for excel, so I have to clean the data with this script
#data is written in the order: year, salary, runs scored, playerid
import csv

list_to_hold_cleaned_data = [] #append the useful values into this list, the program will skip the other ones

counter = 0

with open("C:\Users\Nikhil Gopal\PycharmProjects\sportsstats\salaryandruns.csv") as filehandle_messy_data: #read messy data, append the good data to a list
    read_file_object = csv.reader(filehandle_messy_data, delimiter=',')
    for row in read_file_object:
        if len(row) == 4:
            list_to_hold_cleaned_data.append(row)

filehandle_messy_data.close()

with open('salaryandrunscleaned.csv', 'wb') as filehandle_cleaned_data: #write the good data to a new list
    writer = csv.writer(filehandle_cleaned_data)
    for x in list_to_hold_cleaned_data:
        writer.writerow(x)

filehandle_cleaned_data.close()