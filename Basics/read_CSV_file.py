import csv
'''comment seperated variable'''

with open('CSV_example.csv') as csvfile:
    readCSV=csv.reader(csvfile,delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        print(row)
        '''print(row[0],row[1])'''
        d = row[0]
        c = row[3]
        dates.append(d)
        colors.append(c)
    print(dates)

    whatcolor=input('what color do you want to know date?')
    color_index=colors.index(whatcolor.lower())
    '''It will convert all leter into lower case'''
    dt=dates[color_index]
    print(dt)
