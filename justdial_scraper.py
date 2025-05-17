import argparse
import csv
import time
import random
import signal
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Global flag for graceful shutdown
shutdown_flag = False

def signal_handler(sig, frame):
    global shutdown_flag
    print("\nShutting down gracefully...")
    shutdown_flag = True

signal.signal(signal.SIGINT, signal_handler)

parser = argparse.ArgumentParser()
parser.add_argument('--url', help='Enter the url you want to scrape')
parser.add_argument('--file', help='Specify the file name', default="output.csv")
args = parser.parse_args()

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)

def human_scroll(driver):
    scroll_pause = random.uniform(0.5, 1.2)
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    for _ in range(random.randint(3, 5)):
        scroll_amount = random.randint(500, 1000)
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        time.sleep(scroll_pause)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def click_show_numbers(driver):
    buttons = driver.find_elements(By.CSS_SELECTOR, 'div.greenfill_animate.callbutton')
    for btn in buttons:
        try:
            if "Show Number" in btn.text:
                driver.execute_script("arguments[0];", btn)
                time.sleep(random.uniform(0.1, 0.3))
        except:
            continue

def save_data(data, filename):
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Name', 'Phone', 'Rating', 'Address'])
        writer.writerow(data)

def scrape_page(driver, seen):
    try:
        human_scroll(driver)
        
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        listings = soup.find_all('div', class_='resultbox_info')
        
        new_data = []
        for listing in listings:
            try:
                name = listing.find('div', class_='resultbox_title_anchor').text.strip()
                if name in seen:
                    continue
                
                data = {
                    'Name': name,
                    'Phone': listing.find('span', class_='callcontent').text.strip(),
                    'Rating': listing.find('div', class_='resultbox_totalrate').text.split()[0],
                    'Address': listing.find('div', class_='locatcity').text.strip()
                }
                new_data.append(data)
                seen.add(name)
            except Exception as e:
                continue
        
        return new_data
    except Exception as e:
        print(f"Scraping error: {str(e)}")
        return []

def main():
    driver = setup_driver()
    seen = set()
    
    try:
        # Load existing data
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                seen = {row['Name'] for row in reader}
        except FileNotFoundError:
            pass
        
        driver.get(args.url)
        time.sleep(3)
        
        # Create file with headers if new
        with open(args.file, 'a', newline='', encoding='utf-8') as f:
            if f.tell() == 0:
                writer = csv.DictWriter(f, fieldnames=['Name', 'Phone', 'Rating', 'Address'])
                writer.writeheader()

        print("Scraping started... Press Ctrl+C to stop and save")
        
        while not shutdown_flag:
            new_data = scrape_page(driver, seen)
            if new_data:
                for data in new_data:
                    save_data(data, args.file)
                    print(f"Scraped: {data['Name']}")
            
            # Random delay between scrapes
            time.sleep(random.uniform(2, 4))
            
    finally:
        driver.quit()
        print("Browser closed. Final data saved to", args.file)

if __name__ == "__main__":
    main()
