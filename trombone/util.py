import requests


def download_file(url: str, new_file_name: str):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()

        with open(new_file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
