from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader

from core.exceptions import UnauthorizedException
from core.config import get_settings


api_key_header = APIKeyHeader(name="Authorization", auto_error=False)

def verify_token(api_key: str = Security(api_key_header)):
    """
      Verifies the API key parsed in headers
    """
    settings = get_settings()

    if settings.API_KEY != api_key:
        raise UnauthorizedException
    return api_key
