from bs4 import BeautifulSoup
import requests

wsid_item_buffer = []

# capture the html page for consumption
url = input("Input the url: ")
collection_page = requests.get(url)
text_page = collection_page.text
soup = BeautifulSoup(text_page, 'html.parser')

# find all the div tags, then look into the children for the class tag called "collectionItemDetails"
links = soup.find_all('div', {"class": "collectionItemDetails"})

print("Extracting IDs from workshop collection....")
i = 0
while i < len(links):
    find_link = links[i].find("a", href=True)
    wsid_item_buffer.append(str(find_link['href'][55:]))
    i += 1

with open("workshop.lua", 'w') as file:
    for item in wsid_item_buffer:
        print(f"added {item} to workshop.lua...")
        file.write("resource.AddWorkshop(" + '"' + item + '"' + ")" + "\n")

