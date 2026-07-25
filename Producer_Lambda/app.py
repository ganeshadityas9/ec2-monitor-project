import json
import boto3

sqs = boto3.client('sqs')

QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/272795261907/EC2AlertQueue"



# import requests


def lambda_handler(event, context):
    message = {
        "server": "EC2-App-Server",
        "cpu": "85%",
        "status": "High CPU Usage"
    }

    response = sqs.send_message(
        QueueUrl= QUEUE_URL,
        MessageBody=json.dumps(message)
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Message sent to SQS successfully",
            "messageId": response["MessageId"]
        })
    }

