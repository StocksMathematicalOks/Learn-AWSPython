import json
from botocore.vendored import requests
import urllib3
import http.client

from botocore.awsrequest import AWSPreparedRequest
from botocore.awsrequest import AWSResponse


def lambda_handler(event, context):
    url1 = ''
    url2 = ''
    obj1 = composeRequest(url1)
    obj2 = composeRequest(url2)
 
    return {
        'statusCode': 200,
        'body': obj2# json.dumps(data1)
    }

def composeRequest(url):
    conn = http.client.HTTPSConnection('www...')
    conn.request("GET", url)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    data1 = r1.read()
    
    while chunk := r1.read(200):
        print(repr(chunk))
        
    conn.close() 
    return json.loads(data1)
