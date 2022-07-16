import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import json
import datetime
import hashlib
import zoneinfo


def extractUrl( urlFile ):
    urlDict={}
    with open( urlFile, 'r') as file:
        for line in file:
            urlDict[line.rstrip().split()[0]] = line.rstrip().split()[1]

    return urlDict


def prevWeekDay( timeValue ):
    offsets = (3, 1, 1, 1, 1, 1, 2)
    prevWDay = (timeValue - datetime.timedelta(days=offsets[timeValue.weekday()])).replace(minute=0, hour=0, second=0, microsecond=0)

    return prevWDay


def scrapper( url ):

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    #url = 'https://www.smartfit.com.gt/gimnasios/mix-san-cristobal'
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
    except:
        print('Url cannot be opened')
        exit()

    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup.select('article.general_content div[data-react-class="ShowLocations/ShowLocations"]')
    # load json as map
    rawJson = ''.join( [ tag["data-react-props"] for tag in tags ] )
    data = json.loads(rawJson)
    # on map extract .frequencyData.data , .frequency.updatedAt

    #preparing output file
    timestamp = datetime.datetime.now(tz=zoneinfo.ZoneInfo('America/Guatemala'))
    #offsets = (3, 1, 1, 1, 1, 1, 2)
    #prevWeekDay = (timestamp - datetime.timedelta(days=offsets[timestamp.weekday()])).replace(minute=0, hour=0, second=0, microsecond=0)
    printList=[]
    hashsum = hashlib.md5()
    printList.append('# '+ data['name'] +'\n')
    printList.append('# Hora del script: ' + timestamp.isoformat() +'\n')
    printList.append('# Actualización del servidor: ' + data['frequencyData']['updatedAt']+'\n')
    printList.append('# Tiempo'+'\t'+'Unix'+'\t'+'ISO 8601'+'\t'+'Conteo de Entrada'+'\n')

    for time, count in data['frequencyData']['data'].items():
        unixStamp = prevWeekDay(timestamp) + datetime.timedelta( hours=int(time) )
        printList.append( str(time) +'\t'+ str(unixStamp.timestamp() ) + '\t'+ str(unixStamp.isoformat()) + '\t' + str(count)+'\n')
        #calculate md5 sum for the raw data
        hashsum.update( str(time).encode() + str(count).encode() )

    #md5 sum is always at the bottom of the output
    printList.append( '#' + hashsum.hexdigest() )

    return printList
