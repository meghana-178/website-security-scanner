# Placeholder for app/utils.py

import requests
import ssl
import socket
from urllib.parse import urlparse
import whois

def scan_website(url):
    if not url.startswith('http'):
        url = 'http://' + url

    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    result = {
        'url': url,
        'https': url.startswith('https'),
        'ssl_valid': False,
        'headers': {},
        'domain_info': {},
        'error': None
    }

    # SSL check
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                result['ssl_valid'] = True if cert else False
    except Exception:
        result['ssl_valid'] = False

    # Header check
    try:
        r = requests.get(url, timeout=5)
        result['headers'] = {k: r.headers.get(k) for k in [
            'Content-Security-Policy', 'X-Frame-Options', 'Strict-Transport-Security']}
    except Exception as e:
        result['error'] = str(e)

    # Domain info
    try:
        domain_info = whois.whois(hostname)
        result['domain_info'] = {
            'domain_name': domain_info.domain_name,
            'creation_date': domain_info.creation_date,
            'expiration_date': domain_info.expiration_date
        }
    except Exception:
        result['domain_info'] = {}

    return result
