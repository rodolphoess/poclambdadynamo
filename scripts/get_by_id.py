import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    table = client.Table('flights')
    
    response = table.get_item(
        Key={
            'id': 'AA111'
        }    
    )
    
    print(response['Item'])
