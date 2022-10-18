import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    table = client.Table('flights')
    
    response = table.scan()
    
    print(response['Items'])
