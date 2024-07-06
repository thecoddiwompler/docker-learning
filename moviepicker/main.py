import requests

def main():
    # Make a GET request to a public API (example: JSONPlaceholder)
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()  # Parse JSON response
        print(f"Title: {data['title']}")
        print(f"Body: {data['body']}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

if __name__ == '__main__':
    main()