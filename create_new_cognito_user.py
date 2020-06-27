import json
import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')
accesskey = "XXX"
secretaccesskey = "XXX"
region = "XXX"
session = boto3.Session(aws_access_key_id=accesskey, aws_secret_access_key=secretaccesskey, region_name=region)
client = boto3.client('cognito-idp', region_name=region)
poolId = "XXX" 
email = "XXX"
group = "XXX"

def lambda_handler():
	# DataSet

    resp = client.admin_create_user(
            UserPoolId =poolId,
            Username ="XXX",
            UserAttributes =[
                {
                    'Name':'email',
                    'Value':'nishith2121@gmail.com'
                },
                {
                    'Name':'phone_number',
                    'Value':'+916351151469'
                },
                {
                    'Name':'phone_number_verified',
                    'Value':'false'
                },
                {
                    'Name':'email_verified',
                    'Value':'true'
                },
                {
                    'Name':'given_name',
                    'Value':'XXX'
                }
            ],
            MessageAction ='SUPPRESS',
            DesiredDeliveryMediums = ['EMAIL'],
            TemporaryPassword ='Diwali2020'
        )
    print(resp)

lambda_handler();
