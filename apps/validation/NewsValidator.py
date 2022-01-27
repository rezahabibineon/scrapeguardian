import re
import requests
from urllib.parse import urlparse


def validate_link(link):
    parser = urlparse(link)
    suburl = 'www.theguardian.com' in link
    regexs = re.compile(".+://www.theguardian.com/.+/.+/.+/.+/.+")
    
    if not all([parser.scheme, parser.netloc]):
        return False, 'invalid url. the url should be https://www.*.com!'

    if not suburl:
        return False, 'invalid url. the url should contain www.theguardian.com!'

    if not bool(re.match(regexs, link)):
        return False, 'invalid url. the url should be https://www.theguardian.com/{category}/{year}/{month}/{date}/*'

    if requests.get(link).status_code != 200:
        return False, 'url requested not found'

    return True, 'url found in site'    
