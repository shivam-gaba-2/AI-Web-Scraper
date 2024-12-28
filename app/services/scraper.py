from bs4 import BeautifulSoup
import requests

from core.constants import Constants
from services.analyze import Analyze
from core.exceptions import InvalidUrlException, RequestTimeoutException


def scrape_homepage(url: str) -> str:
    try:
        response = requests.get(url, timeout=20)
    except requests.exceptions.Timeout as e:
        raise RequestTimeoutException from e

    if response.status_code != 200:
        return InvalidUrlException

    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text(separator=' ', strip=True)
    content_analyzer = Analyze(text)

    return {
        "industry": content_analyzer.analyze_data(Constants.INDUSTRY),
        "company_size": content_analyzer.analyze_data(Constants.SIZE),
        "location": content_analyzer.analyze_data(Constants.LOCATION),
    }
