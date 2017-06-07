####AUTHOR/CREDIT: O'Brien, Oliver (o.obrien@ucl.ac.uk)

#Paramters: startID (in order of the london.csv file - not necc numerical order!), maxID

import csv
import os
import sys



def routing():
    locations = []
    maxID = int(sys.argv[3])

    csvreader = csv.reader(open('london.csv', 'r'))
    for row in csvreader:
        locations.append([row[0], row[3], row[4]])

    started = False
    for start in locations:
        startID = int(start[0])
        if int(sys.argv[1]) == startID:
            started = True
        if int(sys.argv[2]) == startID:
            started = False
        if started == True:
            print "***************" + str(startID) + "***************"
            for end in locations:
                endID = int(end[0])
                if startID != endID and startID <= maxID and endID <= maxID:
                    fname = str(startID) + "_" + str(endID) + ".txt"

    if os.path.exists("../routes/results_londonr6/" + fname) == False:
        print "Trying " + str(startID) + " to " + str(endID)
        cmd = "../routes/routino-2.7.2/web/bin/router --transport=bicycle --quiet --lon1=" + start[2] + " --lat1=" + start[1] + " --lon2=" + end[2] + " --lat2=" + end[1] + " --shortest --output-text-all"
        os.system(cmd)
        os.rename("shortest-all.txt", "../routes/results_londonr6/" + fname)
