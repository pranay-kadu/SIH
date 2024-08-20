import requests
from bs4 import BeautifulSoup
import os

def download_html_css_js(url):
    """Downloads HTML, CSS, and JS files from a given URL.

    Args:
        url (str): The URL of the website to scrape.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for error HTTP statuses
        soup = BeautifulSoup(response.content, 'html.parser')

        # Create directories for CSS and JS files
        os.makedirs('output', exist_ok=True)
        css_dir = 'output/css'
        js_dir = 'output/js'
        os.makedirs(css_dir, exist_ok=True)
        os.makedirs(js_dir, exist_ok=True)

        # Save HTML to sample.html
        with open('sample.html', 'w', encoding='utf-8') as f:
            f.write(str(soup))

        # Download CSS and JS (rest of the code remains the same)
        # ...

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")

if __name__ == '__main__':
    url = 'https://colorlib.com/etc/lf/Login_v16/index.html'  # Replace with the target URL
    download_html_css_js(url)