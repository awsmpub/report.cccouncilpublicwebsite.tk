import boto3
import os
import json

dynamodb = boto3.client('dynamodb')

def handler(event, context):
    result = dynamodb.scan(
        TableName = os.environ['DYNAMODB_TABLE']
    )
    traffic_stats = []
    for item in result["Items"]:
        traffic_stats.append({
            "statName": item["statName"]["S"],
            "statValue": item["statValue"]["S"]
        })

    response = {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'application/json',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
        "body": json.dumps(traffic_stats)
    }

    # response = {
    #     "statusCode": 200,
    #     "headers": {
    #         'Access-Control-Allow-Origin': '*',
    #         'Access-Control-Allow-Headers': 'application/json',
    #         'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    #         },
    #     "body": json.dumps('Hello from Lambda!')
    # }

    return response