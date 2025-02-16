import json 
import boto3

dynamodb = boto3.resource('dynamodb',region_name='us-east-1')

def lambda_handler(event,context):
    table = dynamodb.Table('serverless')
    response = table.scan()
    data = response['Items']
    
    while 'LastEvaluateKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluateKey'])
        data.Extend(response['Items'])
    return data