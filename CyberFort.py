import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse

# Current Google Safe Browsing API Key
GOOGLE_API_KEY = "AIzaSyA3xu3kPj8qhwFzPwnsw4wUivRy9zZ2X7M"
SAFE_BROWSING_URL = "https://safebrowsing.googleapis.com/v4/threatMatches:find"

def check_url_with_google_safe_browsing(url):
    payload = {
        "client": {
            "clientId": "yourcompanyname",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["WINDOWS"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": url}
            ]
        }
    }
    params = {'key': GOOGLE_API_KEY}
    response = requests.post(SAFE_BROWSING_URL, json=payload, params=params)
    threat_matches = response.json().get('matches')
    if threat_matches:
        return True, threat_matches
    return False, None

def format_url(url):
    if not re.match(r'http(s?)://', url):
        return f'http://{url}'
    return url

def is_suspicious_url(url):
    suspicious_patterns = [
    ]
    for pattern in suspicious_patterns:
        if re.search(pattern, url):
            return True
    return False

def check_iframes_for_external_links(soup, main_page_url):
    iframes = soup.find_all('iframe')
    for iframe in iframes:
        src = iframe.get('src', '')
        if not src.startswith('http') or domain_differs(src, main_page_url):
            return True
    return False

def domain_differs(url1, url2):
    def get_domain(url):
        parsed_url = urlparse(url)
        return f'{parsed_url.scheme}://{parsed_url.netloc}'

    domain1 = get_domain(url1)
    domain2 = get_domain(url2)

    return domain1 != domain2

def check_for_phishing_keywords(soup):
    keywords = ['login', 'password', 'verification', 'update', 'account']
    text = soup.get_text().lower()
   
    for keyword in keywords:
        if keyword in text:
            return True
    return False

def analyze_webpage_content(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')

        if check_iframes_for_external_links(soup, url):
            return "Suspicious iframes detected."

        if check_for_phishing_keywords(soup):
            return "Phishing keywords detected."

        return None
    except requests.RequestException as e:
        return f"Error analyzing webpage: {e}"

def is_phishing(url):
    url = format_url(url)
    if is_suspicious_url(url):
        return "URL pattern is suspicious."
    safe_browsing_check, threat_info = check_url_with_google_safe_browsing(url)
    if safe_browsing_check:
        return f"Google Safe Browsing has detected issues: {threat_info}"

    content_analysis = analyze_webpage_content(url)
    if content_analysis:
        return content_analysis

    return "URL does not appear to be suspicious."

def main():

    RED_TEXT = "\033[1;31m"
    RESET_TEXT = "\033[0m"

    print("------------------------------------------------")    
    print(RED_TEXT + "CyberFort: Phishing Link Detector" + RESET_TEXT)
    print("------------------------------------------------")
    print("Developed by BLVK3AT")
    print("Note: This is a basic tool. Contributions to enhance it are welcome!")
    print("For more information, visit: github.com/blvk3at")
    print("------------------------------------------------")
    while True:
        url_input = input("Enter the URL to check (or 'exit' to quit): ")
        if url_input.lower() == 'exit':
            break
        url = format_url(url_input)
        result = is_phishing(url)
        print(f"Result: {result}\n")

if __name__ == "__main__":
    main()
