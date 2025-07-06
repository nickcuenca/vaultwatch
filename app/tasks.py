from celery import Celery
import os
import boto3

celery_app = Celery(__name__, broker=os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0"))

@celery_app.task
def send_alert(alert_type: str, user_id: int):
    # Placeholder: Send email via AWS SES
    ses = boto3.client(
        'ses',
        aws_access_key_id=os.getenv("AWS_SES_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SES_SECRET_ACCESS_KEY"),
        region_name='us-east-1'
    )
    sender = os.getenv("EMAIL_SENDER")
    recipient = sender
    subject = f"VaultWatch Alert: {alert_type}"
    body = f"Alert triggered for user {user_id}: {alert_type}"

    ses.send_email(
        Source=sender,
        Destination={'ToAddresses': [recipient]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': body}}
        }
    )