#author = Nikhil Gopal
import csv

#dictionary key is the player id, values are: year, salary, runs

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


with open('salaryandruns.csv', 'wb') as f:
    writer = csv.writer(f)
    for x in dictionary:
        y = dictionary[x]
        if type(y) == list:
            y.append(x)
            writer.writerow(y)
        else:
            pass


f.close()







