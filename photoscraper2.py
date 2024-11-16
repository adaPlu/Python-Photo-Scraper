from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#BuiltBy:AdaPluguez
#2/24/2024
import time
import os
import requests
from PIL import Image
from io import BytesIO

def download_image(image_url, folder_path, img_name):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    try:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.save(os.path.join(folder_path, img_name))
        print(f"Downloaded {img_name}")
    except Exception as e:
        print(f"Could not download {image_url}. Reason: {e}")

def scroll_to_bottom(driver):
    html = driver.find_element(By.TAG_NAME, 'html')
    old_position = 0
    new_position = None
    while new_position != old_position:
        old_position = driver.execute_script("return window.pageYOffset;")
        html.send_keys(Keys.PAGE_DOWN)  # Simulate pressing the END key
        time.sleep(60)  # Adjust time as necessary
        new_position = driver.execute_script("return window.pageYOffset;")

def scrape_photos(url, folder_path):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    
    # Wait for the initial images to load and scroll to the bottom of the page
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "img")))
    scroll_to_bottom(driver)
    
    # Find all image elements
    images = driver.find_elements(By.TAG_NAME, "img")
    photo_urls = [img.get_attribute('src') for img in images if img.get_attribute('src')]
    
    # Download each image
    for i, img_url in enumerate(photo_urls):
        download_image(img_url, folder_path, f"image_{i}.jpg")
    
    driver.quit()  # Close the browser

#url = 'https://rec.net/user/Perkys/photos'
url = 'https://rec.net/user/Daleana/photos'
folder_path = 'downloaded_images'
scrape_photos(url, folder_path)
