import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv('API.env')

class Config:
    OPENWEATHER_API_KEY_ENV = "OPENWEATHER_API_KEY"
    EMAIL_USER_ENV = "EMAIL_USER"
    EMAIL_PASSWORD_ENV = "EMAIL_PASSWORD"

    def __init__(self):
        self.API_KEY = os.getenv(self.OPENWEATHER_API_KEY_ENV)
        self.EMAIL_USER = os.getenv(self.EMAIL_USER_ENV)
        self.EMAIL_PASSWORD = os.getenv(self.EMAIL_PASSWORD_ENV)
        self.CACHE_TIMEOUT = 1800  # Cache timeout in seconds (30 minutes)
        self.BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
        self.FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"
        self.CACHE_DIR = "cache"
    def is_valid(self):
        """
        Check if the configuration is valid.

        Returns:
            bool: True if all required environment variables are set, False otherwise.
        """
        return all([
            self.API_KEY,
            self.EMAIL_USER,
            self.EMAIL_PASSWORD
        ])

config = Config()
