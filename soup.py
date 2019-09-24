import json
import sys
from bs4 import BeautifulSoup
import requests
import re


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
    footer = souped_html_content.find(id="footer")
    footer_2 = footer.find_all('div', class_='span4')
    print("\nTitle:     ", souped_html_content.title.string)
    print("Address:   ", footer_2[0].a.text)
    print("Phone:     ", footer_2[1].a.text)
    print("Email:     ", footer_2[1].findAll('a')[1].text)
    print("\nUpper nav menu items:")
    for item in souped_html_content.find(id="menu-table").find_all(class_="menu-key"):
        print(" ▫️ ", item.text.strip())
    print("\nProperties that have href's:")
    for link in souped_html_content.find_all('a', attrs={'href': re.compile("^(https)|(http)")}):
        print(" ▫️ ", link.get('href'))
    print("\nHref of 'UFMail' button: ", souped_html_content.find(id='ufmail_')['href'])
    print("\nHref of 'MiU' button: ", souped_html_content.find(id='miu_')['href'])
    print("\nHref of all <img>:")
    img_count = 0
    for img in souped_html_content.find_all('img', attrs={'src': re.compile("^(https)|(http)|(/)")}):
        print(" ▫️ ", img.get('src'))
        img_count += 1
    print("\nCount of all <img>: ", img_count)


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


# soup_test = soup_html_content("http://ufm.edu/Portal")
portal()
