import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    client_dynamo=boto3.resource('dynamodb')
    table=client_dynamo.Table('flights')
    try:
        response=table.put_item(Item=event)
        return "Done!"
    except:
        raise
