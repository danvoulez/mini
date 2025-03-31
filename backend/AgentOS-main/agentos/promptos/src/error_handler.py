
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from logger import logger

class GlobalExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            logger.exception("Unhandled error")
            return JSONResponse(
                status_code=500,
                content={"detail": "An unexpected error occurred", "error": str(e)}
            )
