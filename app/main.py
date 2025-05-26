"""
Aplicación principal de FastAPI
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas de la API
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    """
    Endpoint raíz de la aplicación
    """
    return {
        "message": "¡Bienvenido a la API FastAPI!",
        "version": settings.VERSION,
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """
    Endpoint para verificar el estado de la aplicación
    """
    return {"status": "healthy"} 