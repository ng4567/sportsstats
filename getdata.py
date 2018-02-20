#author = Nikhil Gopal
import csv

#dictionary key is the player id, values are: year, salary, runs, playerid, salary adjusted for inflation

dictionary = {}

with open("C:\Users\Nikhil Gopal\PycharmProjects\sportsstats\salaries.csv") as salariesfile:
    readSalariesFile = csv.reader(salariesfile, delimiter=',')
    for row in readSalariesFile:
        playerid = row[0] + row[3]
        salary = row[4]

        dictionary[playerid] = [row[0], salary]



salariesfile.close()

with open("C:\Users\Nikhil Gopal\PycharmProjects\sportsstats\satting.csv") as battingfile:
    readBattingFile = csv.reader(battingfile, delimiter=',')
    for row in readBattingFile:
        playerid = row[1] + row[0]

        if dictionary.has_key(playerid) == True:
            runs = row[7]
            dictionary[playerid].append(runs)
        else:
            pass




battingfile.close()


for key in dictionary: #cleaning the dictionary of the instances where there are two numbers of run
    y = dictionary[key]
    if len(y) == 4:
        third_value = y[2]
        fourth_value = y[3]

#always taking the smaller number of runs

        if third_value < fourth_value: #if the fourth value is greater than delete is
            dictionary[key] = y.pop() #pop() removes the last item in the list with no argument, so removing the fourth value
        else:
            y.pop(2) #if the third value is greater than delete it

    else:
        pass

#the salary data used in this project ranges from years 1985 to 2016, this script will convert all dollars to 2016 dollars
'''
To convert to 2016 dollars:

cpi of base year * salary / cpi of the salary year
http://www.usinflationcalculator.com/inflation/consumer-price-index-and-annual-percent-changes-from-1913-to-2008/
'''
#dictionary that holds all the CPI values per year
cpi_values_by_year = {'1985': 107.6, '1986': 109.6, '1987': 113.6, '1988': 118.3, '1989': 124, '1990': 130.7, '1991': 136.2, '1992': 140.3, '1993': 144.5, '1994': 148.2, '1995': 152.4, '1996': 156.9, '1997': 160.5, '1998': 163, '1999': 166.6, '2000': 172.2, '2001': 177.1, '2002': 179.9, '2003': 184, '2004': 188.9, '2005': 195.3, '2006': 201.6, '2007': 207.3, '2008': 215.303, '2009': 214.537, '2010': 218.056, '2011': 224.939, '2012': 229.594, '2013': 232.957, '2014': 236.736, '2015': 237.017, '2016': 240.007}


with open('salaryandruns.csv', 'wb') as f:
    writer = csv.writer(f)
    for x in dictionary:

        y = dictionary[x]

        if type(y) == list:

            y.append(x) #append the key to the end of the dictionary

#CPI of base year (2016): 240.007, salary is the second valuee in the list, or index 1



            z = 240.007 * int(y[1])
            a = z / cpi_values_by_year[y[0]]
            y.append(a)

            writer.writerow(y)
        else:
            pass


f.close()







