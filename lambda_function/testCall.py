from scrapSmartFit import *

def extractUrl( urlFile ):
    url={}
    with open( urlFile, 'r') as file:
        for line in file:
            url[line.rstrip().split()[0]] = line.rstrip().split()[1]

    return url

filename = "urls.txt"
test=scrapper('https://www.smartfit.com.gt/gimnasios/mix-san-cristobal')
stringOut = ''.join(test)
print(stringOut)
