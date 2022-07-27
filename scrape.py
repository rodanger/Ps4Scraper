from bs4 import BeautifulSoup
import requests
from csv import writer

print()
print("******************************************")


# God of War 4 ps4 URL for scrape

url= "https://store.playstation.com/en-us/search/god%20of%20war" # url from ps4 store
page = requests.get(url)
print(page)

print()

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_="search-results")

print()

# Variables title and price with true label 

with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Location']
    thewriter.writerow(header) # Write the header rows to CSV file

    for list in lists:
        title = list.find('span', class_="psw-t-body psw-c-t-1 psw-t-truncate-2 psw-m-b-2").text 
        price = list.find('span', class_="psw-m-r-3").text
       
        info = [title, price]
        thewriter.writerow(info)  # Write the info rows to CSV file
        print(info)

print()

print("******************************************")

# End