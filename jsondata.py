#Example for parsing and processing JSON

import urllib.request
import json

def printResults(data):
    #Use Json module to load the string data into a dictionary
    theJson = json.loads(data)

    #now we can access the contents of the JSON like any other Python object
    if "title" in theJson["metadata"]:
        print(theJson["metadata"]["title"])

    #output the number of events, plus the magnitude and each event name.
    count = theJson["metadata"]["count"]
    print(str(count) + " events occured")

    #for each event, print the place where it occurred.
    for i in theJson["features"]:
        print(i["properties"]["place"])
    print("--------\n")

    #print the events that only have a magnitude more than 4
    for i in theJson["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("%2.1f" % i["properties"]["mag"], i["properties"]["mag"])
    print("--------\n")

    #print only the events where atleast 1 person reported feeling something
    print("Events that were felt:")
    for i in theJson["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
                print("%2.1f" % i["properties"]["mag"], i["properties"]["mag"],
                " reported " + str(feltReports) + " times")


def main():
    #define a variable to hold the source URL
    #In this case we'll use the free data from USGS
    #This feed lists all earthquakes for the last day larger than mag  2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    #open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print("result code: " + str(webUrl.getcode()))
    if(webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Received error, cannot parse results")    

main()