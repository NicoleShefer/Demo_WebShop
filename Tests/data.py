import os
from dotenv import load_dotenv

load_dotenv()
VALID_EMAIL = os.getenv("TEST_USER_EMAIL")
VALID_PASSWORD = os.getenv("TEST_USER_PASSWORD")
WRONG_PASSWORD = os.getenv("TEST_USER_WRONG_PASSWORD")
UNREGISTERED_EMAIL = os.getenv("TEST_UNREGISTERED_EMAIL", "nobody_registered@example.com")

# invalid data - invalid format of email
INVALID_EMAIL = "test1gg.com"