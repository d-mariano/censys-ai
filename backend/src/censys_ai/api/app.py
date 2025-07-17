from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from censys_ai.api.routes.summarization import router as summarization_router

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="Censys AI Summarization Agent",
    description="API for summarizing Censys cybersecurity data",
    version="0.1.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "version": app.version,
    }

app.include_router(summarization_router, prefix="/summarization", tags=["summarization"] )
