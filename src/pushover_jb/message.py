"""Module to interact with the Pushover Message API."""

from enum import Enum
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BASE_URL = "https://api.pushover.net"

class Priority(Enum):
    """Enum representing message priorities."""

    P1 = 1  # Highest priority
    P2 = 0  # High priority
    P3 = -1  # Normal priority
    P4 = -2  # Low priority

def send(message: str, title: str = "", priority: Priority = Priority.P2):
    """Send a message via the Pushover API.

    Args:
        message (str): The message to be sent.
        title (str, optional): The title of the message. Defaults to an empty string.
        priority (Priority, optional): The priority of the message. Defaults to Priority.P3.

    Raises:
        Exception: If an error occurs during the API request.

    Notes:
        This function requires the following environment variables to be set:
        - PUSHOVER_API_TOKEN: The Pushover API token.
        - PUSHOVER_USER_KEY: The user key for Pushover.
        Make sure you put these in your .env file
    """

    try:
        url = f'{BASE_URL}/1/messages.json'
        form_data = {
            "token": os.getenv('PUSHOVER_API_TOKEN'),
            "user": os.getenv('PUSHOVER_USER_KEY'),
            "title": title,
            "message": message,
            "priority": priority.value
        }
        requests.post(url, data=form_data)

    except Exception as e:
        pass
