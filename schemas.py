"""
Pydantic schemas for data validation
"""
from pydantic import BaseModel, Field
from typing import Optional

class PlatoBase(BaseModel):
    """
    Base schema for Plato with common fields.
    
    This class contains the basic fields that are shared
    between different Plato schemas.
    
    Attributes:
        name (str): The name of the dish, between 1-100 characters
        precio (float): The price of the dish, must be greater than 0
    """
    name: str = Field(..., description="Name of the dish", min_length=1, max_length=100)
    precio: float = Field(..., description="Price of the dish", gt=0)

class PlatoCreate(PlatoBase):
    """
    Schema for creating a new plato.
    
    Inherits from PlatoBase and includes example data
    for API documentation.
    
    Used when creating a new plato through POST requests.
    """
    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Pizza Margherita",
                "precio": 15.99
            }
        }
    }

class PlatoUpdate(BaseModel):
    """
    Schema for updating an existing plato.
    
    All fields are optional to allow partial updates.
    Only provided fields will be updated in the database.
    
    Attributes:
        name (Optional[str]): Optional new name for the dish
        precio (Optional[float]): Optional new price for the dish
    """
    name: Optional[str] = Field(None, description="Name of the dish", min_length=1, max_length=100)
    precio: Optional[float] = Field(None, description="Price of the dish", gt=0)
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "name": "Pizza Margherita Especial",
                "precio": 18.99
            }
        }
    }

class Plato(PlatoBase):
    """
    Complete plato schema with ID.
    
    This schema represents a complete plato as stored in the database,
    including the unique identifier.
    
    Attributes:
        id (int): Unique identifier for the dish, must be greater than 0
        name (str): Inherited from PlatoBase
        precio (float): Inherited from PlatoBase
    """
    id: int = Field(..., description="Unique ID of the dish", gt=0)
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "name": "Pizza Margherita",
                "precio": 15.99
            }
        }
    }

class PlatoResponse(Plato):
    """
    Response schema for plato endpoints.
    
    This schema is used for API responses. Currently identical
    to the Plato schema but can be extended with additional
    response-specific fields if needed.
    
    Inherits all attributes from Plato class.
    """
    pass 