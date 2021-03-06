import json
import boto3

# service object this time for dynamodb
dynamodb = boto3.resource('dynamodb')
# table from dynamodb that we'll be using
table = dynamodb.Table('planets')


def lambda_handler(event, context):
    response = table.get_item(
        Key={
            'id': 'mercury'
        }
    )
    print(response)
    return {
        'statusCode': 200,
        'body': response,
    }
