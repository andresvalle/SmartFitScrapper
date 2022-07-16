from scrapSmartFit import *
import boto3

s3 = boto3.client('s3')

def lambda_handler( event, context ):
    bucket = 'data-dump01'
    #Read urls from S3
    urlFile = 'urls.txt'
    responseInput = s3.get_object(Bucket=bucket, Key=urlFile)
    url = responseInput['Body'].read().decode('utf-8')

    #Split urls and keywords
    urlDict={}
    for line in url.splitlines():
        urlDict[line.rstrip().split()[0]] = line.rstrip().split()[1]

    #For each url, scrap the site and save results to S3
    for key,value in urlDict.items():
        timestamp = datetime.datetime.now(tz=zoneinfo.ZoneInfo('America/Guatemala')).replace(microsecond=0)
        #timestamp = datetime.datetime.now().replace(microsecond=0).isoformat()
        outFile = 'scraps/' + key + '_' + timestamp.strftime('%Y-%m-%dT%H-%M-%S%z') + '.tsv' 
        uploadBytesStream = bytes(''.join(scrapper(value)).encode('UTF-8'))
        s3.put_object( Bucket=bucket, Key=outFile, Body=uploadBytesStream)
        print('Fin ' + key )
