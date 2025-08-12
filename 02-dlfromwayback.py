import subprocess
from datetime import datetime
from urllib.parse import urlparse

def clean_url(url):
    """
    Prepares the URL for Wayback Machine download.
    Removes the last segment if it ends with '.htm' and strips 'http://'.
    """
    url_ready_for_waybback = url.split("/")
    if ".htm" in url:
        url_ready_for_waybback.pop()
    url_ready_for_waybback = "/".join(url_ready_for_waybback)
    return url_ready_for_waybback.replace("http://","")



def download_from_wayback(file_path):
    """
    Reads URLs from a file and downloads their archived versions
    from the Wayback Machine using the wayback_machine_downloader gem.
    """

    with open(file_path, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]

    for url in urls:
        print(datetime.now().strftime("[%H:%M:%S]"), clean_url(url))

        # Requires prior installation >>gem install wayback_machine_downloader<<
        result = subprocess.run(
        ['wayback_machine_downloader', clean_url(url), "--all-timestamps", "--directory", "output_directory/" + clean_url(url), "--from", "19970000000000", "--to", "20050000000000", "--only", r'/\.zip$/i'], shell=True, capture_output=True, text=True) # modify these values > documentation here : https://github.com/hartator/wayback-machine-downloader

        print(result.stdout)


if __name__ == "__main__":
    chemin_du_fichier = r"S:\\saves\\palm\\WaybackIndexer\\urls.txt"
    download_from_wayback(chemin_du_fichier)
