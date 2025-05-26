"""
Main FastAPI application with all routes
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uvicorn
from settings import settings
from schemas import Plato, PlatoCreate, PlatoUpdate, PlatoResponse

# Create FastAPI application instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    openapi_url="/openapi.json"
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory database simulation
platos_db: List[Plato] = [
    Plato(id=1, name="Pizza Margherita", precio=15.99),
    Plato(id=2, name="Pasta Carbonara", precio=12.50),
    Plato(id=3, name="Ensalada César", precio=8.99)
]

# ==================== BASIC ROUTES ====================

@app.get("/")
async def root():
    """
    Root endpoint of the application.
    
    Returns:
        dict: Welcome message with API information
    """
    return {
        "message": "¡Bienvenido a la API FastAPI!",
        "version": settings.VERSION,
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify application status.
    
    Returns:
        dict: Application health status and version
    """
    return {"status": "healthy", "version": settings.VERSION}

# ==================== PLATOS ROUTES ====================

@app.get("/api/v1/platos", response_model=List[PlatoResponse])
async def get_platos():
    """
    Get all platos from the database.
    
    Returns:
        List[PlatoResponse]: List of all available platos
    """
    return platos_db

@app.get("/api/v1/platos/{plato_id}", response_model=PlatoResponse)
async def get_plato(plato_id: int):
    """
    Get a specific plato by its ID.
    
    Args:
        plato_id (int): The unique identifier of the plato
        
    Returns:
        PlatoResponse: The requested plato
        
    Raises:
        HTTPException: 404 if plato is not found
    """
    plato = next((p for p in platos_db if p.id == plato_id), None)
    if not plato:
        raise HTTPException(status_code=404, detail="Plato not found")
    return plato

@app.post("/api/v1/platos", response_model=PlatoResponse)
async def create_plato(plato: PlatoCreate):
    """
    Create a new plato in the database.
    
    Args:
        plato (PlatoCreate): The plato data to create
        
    Returns:
        PlatoResponse: The created plato with assigned ID
    """
    new_id = max([p.id for p in platos_db], default=0) + 1
    new_plato = Plato(id=new_id, **plato.model_dump())
    platos_db.append(new_plato)
    return new_plato

@app.put("/api/v1/platos/{plato_id}", response_model=PlatoResponse)
async def update_plato(plato_id: int, plato_update: PlatoUpdate):
    """
    Update an existing plato with new data.
    
    Args:
        plato_id (int): The unique identifier of the plato to update
        plato_update (PlatoUpdate): The updated plato data
        
    Returns:
        PlatoResponse: The updated plato
        
    Raises:
        HTTPException: 404 if plato is not found
    """
    plato_index = next((i for i, p in enumerate(platos_db) if p.id == plato_id), None)
    if plato_index is None:
        raise HTTPException(status_code=404, detail="Plato not found")
    
    # Update only the provided fields
    plato_data = platos_db[plato_index].model_dump()
    update_data = plato_update.model_dump(exclude_unset=True)
    plato_data.update(update_data)
    
    updated_plato = Plato(**plato_data)
    platos_db[plato_index] = updated_plato
    return updated_plato

@app.delete("/api/v1/platos/{plato_id}")
async def delete_plato(plato_id: int):
    """
    Delete a plato from the database.
    
    Args:
        plato_id (int): The unique identifier of the plato to delete
        
    Returns:
        dict: Confirmation message with deleted plato information
        
    Raises:
        HTTPException: 404 if plato is not found
    """
    plato_index = next((i for i, p in enumerate(platos_db) if p.id == plato_id), None)
    if plato_index is None:
        raise HTTPException(status_code=404, detail="Plato not found")
    
    deleted_plato = platos_db.pop(plato_index)
    return {"message": f"Plato '{deleted_plato.name}' deleted successfully"}

# ==================== TEST ROUTES ====================

@app.get("/api/v1/test")
async def test_endpoint():
    """
    Test endpoint to verify API functionality.
    
    Returns:
        dict: Test message with environment information
    """
    return {"message": "API working correctly", "environment": settings.ENVIRONMENT}

# ==================== APPLICATION EXECUTION ====================

if __name__ == "__main__":
    """
    Main execution block for running the FastAPI application.
    
    This block runs the uvicorn server with the configured settings
    when the script is executed directly.
    """
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level="info"
    )
