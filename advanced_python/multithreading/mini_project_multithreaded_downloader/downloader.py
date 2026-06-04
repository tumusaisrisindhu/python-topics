import os
import threading
import urllib.request

DOWNLOAD_FOLDER = "downloads"

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def download_file(url):
    try:
        filename = url.split("/")[-1]

        filepath = os.path.join(
            DOWNLOAD_FOLDER,
            filename
        )

        print(f"Downloading {filename}...")

        urllib.request.urlretrieve(
            url,
            filepath
        )

        print(f"Completed {filename}")

    except Exception as e:
        print(f"Error downloading {url}")
        print(e)

def main():

    with open("urls.txt", "r") as file:
        urls = [
            line.strip()
            for line in file
            if line.strip()
        ]

    threads = []

    for url in urls:

        thread = threading.Thread(
            target=download_file,
            args=(url,)
        )

        threads.append(thread)

        thread.start()

    for thread in threads:
        thread.join()

    print("\nAll downloads completed")

if __name__ == "__main__":
    main()