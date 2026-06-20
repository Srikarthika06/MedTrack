import boto3

sns = boto3.client(
    "sns",
    region_name="ap-south-1"
)

TOPIC_ARN = "arn:aws:sns:ap-south-1:820942899382:MedTrack"

def send_notification(message):
    sns.publish(
        TopicArn=TOPIC_ARN,
        Message=message,
        Subject="MedTrack Notification"
    )