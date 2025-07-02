import requests
from bs4 import BeautifulSoup
import csv

url = 'https://example.com'  # Replace with the target URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

data = []
for item in soup.find_all('h2'):  # Adjust the tag as needed
         data.append(item.text)

with open('scraped_data.csv', 'w', newline='') as file:
         writer = csv.writer(file)
         writer.writerow(['Title'])
         for row in data:
             writer.writerow([row])
print("✅ scraped_data.csv created successfully.")
