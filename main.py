import re
from bs4 import BeautifulSoup, SoupStrainer
import requests
import lib

# BIG PROBLEM, ITEMS ARE RANDOMLY DUPLICATING TWICE.

temphold = []
permhold = []

# collection pack
url = 'https://steamcommunity.com/sharedfiles/filedetails/?id=2270313137'  # url = input()
reurl = re.compile(url)  # using this to remove any possibility of the collection link showing up in the txt file
stock_url = re.compile("https://steamcommunity.com/sharedfiles/filedetails/*")  # regex matching to remove all possible links outside of the re.compile

collection_page = requests.get(url)
text_page = collection_page.text
soup = BeautifulSoup(text_page, 'html.parser')


for line in soup.findAll('a', href=True):
    temphold.append(line['href'])

file1 = open("linksonpage.txt", "w")
for line in temphold:
    if re.match(stock_url, line):
        lib.write_to_line(file1, line)
file1.close()

file1 = open("linksonpage.txt", "r")
for line in file1:
    permhold.append(line)
file1.close()

lib.check_for_duplication(permhold)

file1 = open("linksonpage.txt", "w")

for line in permhold:
    file1.write(line)
