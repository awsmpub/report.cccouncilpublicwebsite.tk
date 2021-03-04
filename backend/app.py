# app.py
# Community Traffic Safety Dashboard
# Allows residents to view statistics around Traffic Safety within the city

import os
import boto3

from flask import Flask, jsonify, request
app = Flask(__name__)

# USERS_TABLE = os.environ['USERS_TABLE']
STATS_TABLE = os.environ['STATS_TABLE']
IS_OFFLINE = os.environ.get('IS_OFFLINE')

if(IS_OFFLINE):
    client = boto3.client('dynamodb', region_name='localhost', endpoint_url='http://localhost:8000')
else:
    client = boto3.client('dynamodb')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/stats/<string:stat_id>")
def get_stat(stat_id):
    resp = client.get_item(
        TableName=STATS_TABLE,
        Key={
            'statId': { 'S':stat_id }
        }
    )
    item = resp.get('Item')
    if not item:
        return jsonify({'error': 'Statistic does not exist'}), 404

    return jsonify({
        'statId': item.get('statId').get('S'),
        'statValue': item.get('statValue').get('S')
    })

@app.route("/stats", methods=["POST"])
def create_stat():
    stat_id = request.json.get('statId')
    stat_value = request.json.get('statValue')
    if not stat_id or not stat_value:
        return jsonify({'error': 'Please provide statId and statValue'}), 400

    resp = client.put_item(
        TableName=STATS_TABLE,
        Item={
            'statId': {'S': stat_id },
            'statValue': {'S': stat_value }
        }
    )

    return jsonify({
        'statId': stat_id,
        'statValue': stat_value
    })