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
	try:
            resp = client.admin_create_user(
            UserPoolId =poolId,
            Username ="XXXXX",
            UserAttributes =[
                {
                    'Name':'email',
                    'Value':'XXX'
                },
                {
                    'Name':'phone_number',
                    'Value':'XXXX'
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
                    'Value':'Keval Gosai'
                }
            ],
            MessageAction ='SUPPRESS',
            DesiredDeliveryMediums = ['EMAIL'],
            TemporaryPassword ='Diwali2020'
        )
        print(resp)
    except client.exceptions.ResourceNotFoundException:
        print("ResourceNotFoundException exceptions")
    except client.exceptions.InvalidParameterException:
        print("InvalidParameterException exceptions")
    except client.exceptions.UserNotFoundException:
        print("UserNotFoundException exceptions")
    except client.exceptions.UsernameExistsException:
        print("UsernameExistsException exceptions")
    except client.exceptions.InvalidPasswordException:
        print("InvalidPasswordException exceptions")
    except client.exceptions.CodeDeliveryFailureException:
        print("CodeDeliveryFailureException exceptions")
    except client.exceptions.UnexpectedLambdaException:
        print("UnexpectedLambdaException exceptions")
    except client.exceptions.UserLambdaValidationException:
        print("UserLambdaValidationException exceptions")
    except client.exceptions.InvalidLambdaResponseException:
        print("InvalidLambdaResponseException exceptions")
    except client.exceptions.PreconditionNotMetException:
        print("PreconditionNotMetException exceptions")
    except client.exceptions.InvalidSmsRoleAccessPolicyException:
        print("InvalidSmsRoleAccessPolicyException exceptions")
    except client.exceptions.InvalidSmsRoleTrustRelationshipException:
        print("InvalidSmsRoleTrustRelationshipException exceptions")
    except client.exceptions.TooManyRequestsException:
        print("TooManyRequestsException exceptions")
    except client.exceptions.NotAuthorizedException:
        print("NotAuthorizedException exceptions")
    except client.exceptions.UnsupportedUserStateException:
        print("UnsupportedUserStateException exceptions")
    except client.exceptions.InternalErrorException:
        print("InternalErrorException exceptions")

lambda_handler();
