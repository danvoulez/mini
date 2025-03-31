
from fastapi import FastAPI
from error_handler import GlobalExceptionMiddleware
from logger import logger

app = FastAPI(title="PromptOS")

# Apply error handler middleware
app.add_middleware(GlobalExceptionMiddleware)

@app.on_event("startup")
async def startup_event():
    logger.info("PromptOS is starting...")

@app.get("/status")
async def status():
    logger.info("Status checked.")
    return { "status": "PromptOS is online." }
