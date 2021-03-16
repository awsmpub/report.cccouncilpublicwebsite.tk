import boto3
import os
import json

dynamodb = boto3.client('dynamodb')

def handler(event, context):
    stat_name = json.loads(event['body'])['statName']
    result = dynamodb.update_item(
        TableName=os.environ['DYNAMODB_TABLE'],
        Key={
            'statName':{'S': stat_name}
        },
        UpdateExpression='ADD statValue :inc',
        ExpressionAttributeValues={
            ':inc': {'N': '1'}
        },
        ReturnValues="UPDATED_NEW"
    )
    response = {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps({"statValue": result["Attributes"]["statValue"]["N"]})
    }
    return response