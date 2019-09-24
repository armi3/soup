import json
import sys
from bs4 import BeautifulSoup
import requests


def soup_html_content(url):
    # Make a GET request to fetch the raw HTML content
    try:
        html_content = requests.get(url).text
    except:
        print(f"Unable to get {url}")
        sys.exit(1)
    # Parse the html content, this is the Magic ;)
    souped = BeautifulSoup(html_content, "html.parser")
    return souped


def portal():
    souped_html_content = soup_html_content("http://ufm.edu/Portal")
    print("\nTitle: ", souped_html_content.title.string)
    # print("\nAddress: ", souped_html_content.title.string)
    pass


def studies():
    pass


def computer_science():
    pass


def directory():
    pass


def run_all():
    pass


if len(sys.argv) == 1:
    run_all()
elif sys.argv[1] == 1:
    portal()
elif sys.argv[1] == 2:
    studies()
elif sys.argv[1] == 3:
    computer_science()
elif sys.argv[1] == 4:
    directory()


soup_test = soup_html_content("http://ufm.edu/Portal")
#print(soup_test.prettify())
footer = soup_test.find(id="footer")
footer2 = footer.find_all('div', class_='span4')
print(footer2)
