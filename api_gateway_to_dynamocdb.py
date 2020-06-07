# Fetch songlist from dynamoDB table for queried artist
# 1) Create API Gateway HTTP get request to query songlist
# 2) Create new lambda function to be called on HTTP get request
# 3) lambda function should dynamoDB database for list of songs
# 4) Return songlist
#



import boto3
import json
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
        # 1. Parse Query parameters
        SingerName = event['queryStringParameters']['SingerName']
        print('SingerName' + SingerName)
        
        # 2. Fetch data from dynamoDB
        table = dynamodb.Table('Music')
        response = table.query(
            KeyConditionExpression=Key('Artist').eq(SingerName)
        )
        songList = []
        songs = response['Items']
        for song in songs:
            songList.append(song['songTitle'])
        

        # 3. Construct body of response
        Response = {}
        Response['SingerName'] = SingerName
        Response['Song'] = songList

        # 4. Constuct http response object
        responseObject = {}
        responseObject['statusCode'] = 200
        responseObject['headers'] = {}
        responseObject['headers']['Content-Type'] = 'application/json'
        responseObject['body'] = json.dumps(Response)

        # 5. Return object
        return responseObject
