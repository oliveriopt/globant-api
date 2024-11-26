import os

# Function to manually load .env file
def load_env_file(filepath=".env"):
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            for line in file:
                # Ignore empty lines or comments
                if line.strip() and not line.startswith("#"):
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value

# Load the .env file
load_env_file()


class Config:
    S3_BUCKET = os.getenv('S3_BUCKET')
    S3_ACCESS_KEY = os.getenv('S3_ACCESS_KEY')
    S3_SECRET_KEY = os.getenv('S3_SECRET_KEY')
    S3_REGION = os.getenv('S3_REGION', 'us-east-1')
    
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

print(Config.S3_BUCKET)