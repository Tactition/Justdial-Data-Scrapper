# JustDial Scraper

A Python tool for scraping business information from JustDial.

## Features

- Extracts business names, phone numbers, ratings, and addresses
- Handles pagination automatically
- Implements human-like scrolling behavior to avoid detection
- Saves data to CSV format
- Supports graceful shutdown with Ctrl+C
- Prevents duplicates when resuming scraping

## Requirements

- Python 3.6+
- Chrome browser installed

## Installation

1. Clone this repository or download the script:

```bash
git clone https://github.com/yourusername/justdial-scraper.git
cd justdial-scraper
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install selenium beautifulsoup4 webdriver-manager
```

## Usage

Run the script with the following command:

```bash
python justdial_scraper.py --url "https://www.justdial.com/search-query" --file "output.csv"
```

### Parameters:

- `--url`: The JustDial search URL you want to scrape (required)
- `--file`: Output filename for the CSV data (default: "output.csv")

### Example:

```bash
python justdial_scraper.py --url "https://www.justdial.com/Mumbai/Restaurants" --file "mumbai_restaurants.csv"
```

## How It Works

The scraper works by:

1. Initializing a Chrome browser instance with Selenium
2. Loading the specified JustDial URL
3. Simulating human-like scrolling behavior
4. Extracting business information using BeautifulSoup
5. Saving data incrementally to a CSV file
6. Continuing until manually stopped with Ctrl+C

## Output

The script generates a CSV file with the following columns:
- Name: Business name
- Phone: Phone number
- Rating: Customer rating
- Address: Business address

## Notes

- The script includes anti-detection measures but use responsibly and respect website terms of service
- Running the script multiple times with the same output file will only append new entries (no duplicates)
- Use a VPN if you plan to run extensive scraping sessions
- JustDial's website structure may change over time requiring script updates

## Troubleshooting

If you encounter issues:

1. Make sure Chrome is installed and up to date
2. Check if your internet connection is stable
3. If the website structure changed, the CSS selectors might need updating
4. Ensure you have the necessary permissions to write to the output file location

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for educational purposes only. Use responsibly and in accordance with JustDial's terms of service. The developer is not responsible for any misuse of this tool.
