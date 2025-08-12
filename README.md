A Python-based toolset for extracting URLs from legacy .txt and .zip files, and downloading their archived versions from the Wayback Machine, for recovering Psion Epoc / Sibo software from old CD-ROMs

#Features : 

- Scans directories for .txt files and .zip archives containing text.
- Extracts all valid URLs using regular expressions.
- Downloads archived versions of URLs from the Wayback Machine (1997–2005).
- Cleans and formats URLs for compatibility with wayback_machine_downloader.
- Organizes downloads by domain and timestamp.

#Extract URLs from legacy files
python extract_urls.py
This will scan the specified directory and output a list of URLs to a .txt file.

#Download archived content
python 02-dlfromwayback.py
This reads the list of URLs and downloads their archived versions from the Wayback Machine.

#Configuration
You can modify the following paths and parameters directly in the scripts:
- input_directory: Folder to scan for .txt and .zip files.
- output_urls_file: Destination file for extracted URLs.
- url_file_list: Input file for archived downloads.
- --from / --to: Time range for Wayback Machine snapshots.
- --only: Regex filter for specific file types (e.g., .zip).
