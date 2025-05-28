import os


class UnknownEnvironmentError(Exception):
    """Raised when an unknown environment is encountered."""
    pass


class Environment:
    """
    A class to manage different API environments (dev/prod) based on ENV variable.
    Defaults to 'dev' if ENV variable is not set.
    """
    
    DEV = 'dev'
    PROD = 'prod'
    
    URLS = {
        DEV: "https://playground.learnqa.ru/api_dev",
        PROD: "https://playground.learnqa.ru/api"
    }

    def __init__(self):
        try:
            self.env = os.environ['ENV']
            if self.env not in self.URLS:
                raise UnknownEnvironmentError(f"Unknown environment: {self.env}")
        except KeyError:
            self.env = self.DEV

    def get_base_url(self):
        """Returns the base URL for the current environment."""
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise UnknownEnvironmentError(f"Unknown value of ENV variable: {self.env}")
    
    def __str__(self):
        return f"Environment: {self.env}, Base URL: {self.get_base_url()}"


ENV_OBJECT = Environment()