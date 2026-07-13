import boto3

from config import SNS_TOPIC_ARN, AWS_REGION


sns_client = boto3.client(
    "sns",
    region_name=AWS_REGION
)
sns_client = boto3.client(
    "sns",
    region_name="ap-south-1"
)


def send_low_stock_alert(medicine_name, quantity, threshold):

    message = f"""
LOW STOCK ALERT

Medicine Name:
{medicine_name}

Current Quantity:
{quantity}

Minimum Required:
{threshold}

Please restock this medicine.
"""


    response = sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="Medicine Low Stock Alert",
        Message=message
    )


    print("SNS RESPONSE:")
    print(response)
