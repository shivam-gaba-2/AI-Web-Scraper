from pydantic import BaseModel, HttpUrl


class ScrapeRequest(BaseModel):
    url: HttpUrl


class ScrapeResponse(BaseModel):
    industry: str
    company_size: str
    location: str


class ErrorResponse(BaseModel):
    detail: str
