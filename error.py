class InstagramAutomationError(Exception):
    """Base class for exceptions in this module."""
    
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"InstagramAutomationError: {self.message}"


class AuthenticationError(InstagramAutomationError):
    """Exception raised for authentication errors."""
    
    def __init__(self, message="Authentication failed. Please check your credentials."):
        super().__init__(message)

    def __str__(self):
        return f"AuthenticationError: {self.message}"


class EnvironmentVariableError(InstagramAutomationError):
    """Exception raised for missing environment variables."""
    
    def __init__(self, variable_name):
        message = f"Missing environment variable: {variable_name}"
        super().__init__(message)
        self.variable_name = variable_name

    def __str__(self):
        return f"EnvironmentVariableError: {self.message}"