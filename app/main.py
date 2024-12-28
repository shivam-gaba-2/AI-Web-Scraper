from fastapi import Depends, FastAPI, HTTPException

from core.exceptions import BadRequestException, InvalidUrlException, RequestTimeoutException, UnauthorizedException
from services.auth import verify_token
from services.scraper import scrape_homepage
from models import ErrorResponse, ScrapeRequest, ScrapeResponse


app = FastAPI(title = "AI Website Scraper API", host="0.0.0.0", port = 8000)

@app.post(
    "/scrape",
    response_model=ScrapeResponse,
    responses={
        400: {"description": "Bad Request", "model": ErrorResponse},
        401: {"description": "Unauthorized", "model": ErrorResponse},
        404: {"description": "Invalid URL", "model": ErrorResponse},
        408: {"description": "Request Timeout", "model": ErrorResponse}
    }
)
async def scrape_website(request: ScrapeRequest, token: str = Depends(verify_token)):
    try:
        data = scrape_homepage(request.url)
        return ScrapeResponse(**data)
    except UnauthorizedException as e:
        raise e
    except BadRequestException as e:
        raise e
    except InvalidUrlException as e:
        raise e
    except RequestTimeoutException as e:
        raise e
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
