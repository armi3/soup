import json
from bs4 import BeautifulSoup
import requests

# Make a GET request to fetch the raw HTML content
url = "http://ufm.edu/Portal"
try:
    html_content = requests.get(url).text
except:
    print(f"Unable to get {url}")
    sys.exit(1)

# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")

# print if needed, gets too noisy
# print(soup.prettify())

print(soup.title)
print(soup.title.string)

for div in soup.find_all("div"):
    print(div)
    print("--------------------------")
