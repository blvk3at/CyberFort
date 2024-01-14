# CyberFort: Phishing Link Detector
CyberFort: Phishing Link Detector is a basic yet powerful tool developed to identify potential phishing threats in web URLs. It leverages Google Safe Browser API and various heuristic checks to evaluate URLs and determine if they pose any security risks. This tool is designed for cybersecurity enthusiasts and anyone interested in safeguarding against phishing attempts.

# Features
## 1. Google Safe Browsing Check: 
Integrates with the Google Safe Browsing API to cross-reference URLs against known phishing and malware sites.
## 2. Iframe Analysis: 
Scans web pages for iframes that point to different domains, which could indicate malicious intent.
## 3. Keyword Detection: 
Searches web page content for common phishing keywords like 'login', 'password', and 'account'.
## 4. Domain Comparison: 
Compares the domain of a given URL with the main page’s domain to spot discrepancies.
## 5. User-Friendly Interface:
Enhanced with colored text outputs for better readability and user experience.

# Installation
Clone the Repo:
git clone https://github.com/blvk3at/CyberFort.git
# Install the Required Python Packages:
### pip install requests
### pip install beautifulsoup4
# Usage
### Run the script in your terminal or command prompt. 
### Enter the URL you want to check.

# Contribution
This project is in its early stages and welcomes contributions from the cybersecurity community. Whether it's enhancing existing features, adding new checks, or improving the codebase, your contributions can help make the internet a safer place. Feel free to fork this repository, make your changes, and submit a pull request!
