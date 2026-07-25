import json
import boto3

sns = boto3.client('sns')

TOPIC_ARN = "arn:aws:sns:us-east-1:272795261907:EC2AlertTopic"




def lambda_handler(event, context):
    for record in event["Records"]:
        body = json.loads(record["body"])

        print(body)

        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject="EC2 High CPU Alert",
            Message=json.dumps(body, indent=2)
        )