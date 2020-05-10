# 
# AWS Lambda to read CSV file from s3 bucket and update dynamoDB table with new enteries
# Steps
# 1) Setup AWS S3 bucket using AWS console
# 2) Create dynamoDB table using AWS console
# 3) Create AWS policy for s3,dynamodb,cloud watch logs
# 4) Crate new role role_csvto_dynamoDB and attach with policy defined above
# 5) Create AWS lambda under role of "role_csvto_dynamoDB" and add trigger for s3 bucket update
# 6) Check "cloud watch logs"
#

import boto3

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def questionbank_reader(event, context):
    print(event)
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    obj = s3.get_object(Bucket=bucket,Key=key)
    rows = obj['Body'].read().split('\n')
    table = dynamodb.Table('dynamoDBTableName')
    
    with table.batch_writer() as batch:
        for row in rows:
            batch.put_item(Item={
                'DBSchemafield1':row.split(',')[0],
                'DBSchemafield2':row.split(',')[1]
            })
