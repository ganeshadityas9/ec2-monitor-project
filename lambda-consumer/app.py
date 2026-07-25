import json

def lambda_handler(event, context):

    for record in event["Records"]:

        body = json.loads(record["body"])

        print(body)

    return {
        "statusCode": 200,
        "body": "Messages Processed"
    }