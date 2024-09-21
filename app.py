# app.py
import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Assuming the response is in JSON format
    return None

if __name__ == "__main__":
    # Using a public API that provides fake posts in JSON format for testing purposes
    url = "https://jsonplaceholder.typicode.com/posts"
    data = fetch_data(url)
    if data:
        for post in data[:5]:  # Print only the first 5 posts
            print(f"Post ID: {post['id']}, Title: {post['title']}")
    else:
        print("Failed to fetch data")
