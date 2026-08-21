import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    response = table.update_item(
        Key={'id': 'visitor_count'},
        UpdateExpression='ADD #count :incr',
        ExpressionAttributeNames={'#count': 'count'},
        ExpressionAttributeValues={':incr': 1},
        ReturnValues='UPDATED_NEW'
    )

    count = int(response['Attributes']['count'])

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({'count': count})
    }