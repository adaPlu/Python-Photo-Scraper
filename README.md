Image Scraper using Selenium and PIL
This project is a Python script designed to automate the process of scraping and downloading images from a given webpage. By leveraging the Selenium WebDriver and Pillow (PIL) libraries, the script navigates to the specified URL, scrolls to the bottom of the page to load all content, collects image URLs, and downloads them into a specified folder.

Features
Automatically scrolls to the bottom of the page to load all images.
Extracts image URLs from the webpage.
Downloads images and saves them with custom filenames.
Creates the output directory if it does not exist.
Setup Instructions
Prerequisites
Python (3.7 or later)
Google Chrome Browser
Pip dependencies
Selenium
Pillow (PIL)
Requests
Webdriver Manager
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-repo-name/image-scraper.git
cd image-scraper
Install the required Python dependencies:

bash
Copy code
pip install -r requirements.txt
Make sure Google Chrome is installed on your machine.

Usage
Running the Script
Open the script file image_scraper.py (or similar).

Modify the url and folder_path variables as needed:

python
Copy code
url = 'https://rec.net/user/YourTarget/photos'
folder_path = 'desired_folder_path'
Execute the script:

bash
Copy code
python image_scraper.py
The script will scrape and save images from the specified URL to the defined folder.

File Structure
image_scraper.py: The main Python script.
requirements.txt: Lists all dependencies for the project.
downloaded_images/: Default folder where images will be saved (automatically created).
Code Walkthrough
Main Functions
download_image(image_url, folder_path, img_name)

Downloads and saves a single image from the provided URL to the specified folder.
Creates the folder if it doesn't already exist.
scroll_to_bottom(driver)

Scrolls the webpage to the bottom to ensure all dynamic content (images) is loaded.
scrape_photos(url, folder_path)

Manages the scraping process:
Opens the browser.
Navigates to the given URL.
Collects and downloads all image URLs.
Notes
The script includes error handling for failed image downloads.
Adjust the time.sleep() interval in scroll_to_bottom to optimize performance based on page load times.
Ensure you comply with the website's terms of service before scraping.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Built By: Ada Pluguez
Date Created: February 24, 2024

