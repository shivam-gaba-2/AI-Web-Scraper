# 🚀 FastAPI AI Agent for Website Scraping

## 📚 Objective
Build a FastAPI application that leverages AI to extract meaningful insights from a website's homepage. The agent will analyze the content and answer specific business-related questions.

## 🎯 Features
- ✅ **POST Endpoint for URL Input**
- ✅ **Authorization Header with Secret Key**
- ✅ **Content Analysis with AI Agent**
- ✅ **Pydantic for Data Validation and Response Models**
- ✅ **Error Handling for Invalid or Inaccessible URLs**
- ✅ **Deployment on Railway**

## 🛠️ Tech Stack
- **FastAPI**: Backend framework
- **BeautifulSoup**: Web scraping
- **Pydantic**: Data validation and serialization
- **HTTP Bearer Authentication**: Secure access
- **Deployment**: Railway

## 📥 API Endpoints

### 1️⃣ **POST /scrape**
**Description:** Analyze a website homepage and extract key business information.

**Request Headers:**
```http
Authorization: <SECRET_KEY>
```

**Request Body:**
```json
{
  "url": "https://watchguard.com"
}
```

**Response Example:**
```json
{
  "industry": "Technology",
  "company_size": "Medium",
  "location": "San Francisco, CA"
}
```

**Error Responses:**
- `401 Unauthorized`: UnauthorizedException - Invalid or missing secret key.
- `400 Bad Request`: BadRequestException - Invalid request body.
- `404 Invalid URL`: InvalidUrlException - The provided URL is not valid.
- `408 Request Timeout`: RequestTimeoutException - The request to fetch website data timed out.
- `500 Internal Server Error`: Scraping or processing error.

## 🛡️ Authentication
Set your secret key in the environment variables:
```
SECRET_KEY=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+
```

## 🌐 Live Demo
[Deployed Application Link](https://ai-web-scraper-production.up.railway.app/scrape)

---
**Happy Scraping! 🚀**

