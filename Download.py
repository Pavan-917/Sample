import requests
from bs4 import BeautifulSoup

def get_direct_download_link(url, file_extension=None):
    """
    Extracts direct download links from a webpage.
    Optionally filter by file extension (e.g., '.pdf', '.mp3').
    """
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    links = []

    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('http') or href.startswith('https'):
            if file_extension:
                if href.lower().endswith(file_extension.lower()):
                    links.append(href)
            else:
                links.append(href)
    return links

# Example usage:
if __name__ == "__main__":
    url = input("Enter the webpage URL: ")
    ext = input("Enter file extension to filter (e.g., .pdf) or leave blank for all: ").strip()
    ext = ext if ext else None
    direct_links = get_direct_download_link(url, ext)
    if direct_links:
        print("Direct download links found:")
        for link in direct_links:
            print(link)
    else:
        print("No direct download links found.")