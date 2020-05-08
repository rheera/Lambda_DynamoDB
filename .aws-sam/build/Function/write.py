import boto3

# service object this time for dynamodb
dynamodb = boto3.resource('dynamodb')
# table from dynamodb that we'll be using
table = dynamodb.Table('planets')


def lambda_handler(event, context):
    response = table.put_item(
        Item={
            'id': 'neptune',
            'temp': -214,
        }
    )
    print(response)
    return {
        'statusCode': 200,
        'body': 'Item added',
    }
