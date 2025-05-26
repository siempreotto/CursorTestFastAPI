"""
FastAPI project configuration
"""
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    """
    Application settings configuration class.
    
    This class defines all the configuration parameters for the FastAPI application.
    Settings can be overridden using environment variables or a .env file.
    
    Attributes:
        PROJECT_NAME (str): Name of the FastAPI project
        VERSION (str): Current version of the application
        DESCRIPTION (str): Description of the API
        HOST (str): Host address for the server
        PORT (int): Port number for the server
        DEBUG (bool): Debug mode flag
        ENVIRONMENT (str): Current environment (development, production, etc.)
        ALLOWED_HOSTS (List[str]): List of allowed hosts for CORS
        API_V1_STR (str): API version 1 prefix string
    """
    
    # Project information
    PROJECT_NAME: str = "FastAPI Project"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "API developed with FastAPI"
    
    # Server configuration
    HOST: str = "127.0.0.1"
    PORT: int = 9500  # Changed to a higher port to avoid conflicts
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    
    # CORS configuration
    ALLOWED_HOSTS: List[str] = ["*"]
    
    # Additional configuration
    API_V1_STR: str = "/api/v1"
    
    class Config:
        """
        Pydantic configuration class for Settings.
        
        Defines how the settings should be loaded and validated.
        
        Attributes:
            env_file (str): Path to the environment file
            case_sensitive (bool): Whether environment variables are case sensitive
        """
        env_file = ".env"
        case_sensitive = True

# Global configuration instance
settings = Settings() 