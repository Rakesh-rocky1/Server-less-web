import json 
import boto3

dynamodb =  boto3.resource('dynamodb',region_name='us-east-1')

def lambda_handler(event,context):
    table=dynamodb.Table('serverless')
    firstname = event['firstname']
    message = event['message']
    lastname = event['lastname']
    date = event['date']
    
    response = table.put_item(
        Item={
            'msg': message,
            'firstname': firstname,
            'lastname': lastname,
            'date': date
        }
    )
        
    return {
        'statusCode': 200,
        'body': json.dumps('Message from' +firstname)
    }