📞 ChatGestDial Scraper
A Python-based scraper that fetches phone numbers, emails, ratings, and addresses of businesses listed on ChatGestDial using Selenium and BeautifulSoup. This tool is ideal for digital marketers, lead generation, or local business research.

🚀 Features
✅ Extracts:

Business Name

Phone Number

Rating

Address

✅ Uses Selenium for dynamic JS content

✅ Mimics human scrolling behavior

✅ Graceful shutdown with Ctrl+C

✅ Avoids duplicates by tracking previously scraped names

✅ Output in clean CSV format

📦 Installation
Make sure you have Python 3.7+ installed.

bash
Copy
Edit
git clone https://github.com/your-username/chatgestdial-scraper.git
cd chatgestdial-scraper
pip install -r requirements.txt
requirements.txt
nginx
Copy
Edit
selenium
beautifulsoup4
webdriver-manager
🛠️ Usage
bash
Copy
Edit
python scraper.py --url "https://www.chatgestdial.com/example-category" --file "business_data.csv"
Arguments:
Argument	Description	Required	Default
--url	URL of the ChatGestDial page to scrape	✅	-
--file	Output CSV file name	❌	output.csv

Press Ctrl+C anytime to stop the scraper and save collected data.

💡 How It Works
Launches a Chrome browser in the background using Selenium.

Scrolls the page like a human to load more results.

Locates and clicks “Show Number” buttons.

Extracts visible data using BeautifulSoup.

Appends new entries to a CSV file, skipping duplicates.

📁 Output Format (CSV)
Name	Phone	Rating	Address
Pizza Delight	123-456-7890	4.5	Sector 10, New Delhi
Quick Repair Hub	987-654-3210	3.8	MG Road, Bengaluru

⚠️ Disclaimer
This project is intended for educational and ethical use only.
Do not use this tool to violate the ChatGestDial Terms of Service.
You are solely responsible for how you use this script.

🤖 Author
Tactition
Built with 💻, ☕, and a dash of curiosity.
