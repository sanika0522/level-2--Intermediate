import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for post in data[:5]:  # Print first 5 posts
        print(f"Title: {post['title']}\n")
else:
    print("Failed to fetch data:", response.status_code)
