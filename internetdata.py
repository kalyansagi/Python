#Example file for retrieving data from internet

import urllib.request

def main():
    webUrl = urllib.request.urlopen("http://www.google.com")
    print("result code: " + str(webUrl.getcode()))
    data = webUrl.read()
    print("data is: " + str(data))
    #print(data)



main()
