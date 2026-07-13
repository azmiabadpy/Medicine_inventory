import os
from dotenv import load_dotenv

load_dotenv()


DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = int(os.getenv("DB_PORT", 3306))


AWS_REGION = os.getenv(
    "AWS_REGION",
    "ap-south-1"
)


SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")


FLASK_SECRET_KEY = os.getenv(
    "FLASK_SECRET_KEY"
)
