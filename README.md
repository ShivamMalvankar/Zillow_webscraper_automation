# Zillow Data Automation Bot 🏠🤖

##  Overview

This project automates the process of collecting real estate data from Zillow and storing it in a structured format using Google Forms.

It uses **BeautifulSoup** for web scraping and **Selenium** for browser automation.

---

##  Features

* Scrapes property data from Zillow:

  * 🏷️ Prices
  * 📍 Addresses
  * 🔗 Property links
* Automatically fills a Google Form with the collected data
* Handles multiple listings efficiently
* End-to-end automation pipeline

---

##  Tech Stack

* Python 
* BeautifulSoup (bs4) 
* Selenium WebDriver 

---

##  How It Works

1. Sends a request to Zillow and fetches HTML data
2. Uses BeautifulSoup to extract:

   * Property prices
   * Addresses
   * Listing URLs
3. Launches a browser using Selenium
4. Automatically fills the Google Form for each property

---

##  Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/zillow-data-automation.git
cd zillow-data-automation
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the script

```bash
python main.py
```

---

##  Important Notes

* Zillow may block requests if too many are sent → use delays if needed
* Make sure ChromeDriver is installed and matches your Chrome version
* Google Form structure should match the automation script

---

##  Future Improvements

* Add CAPTCHA handling
* Store data in CSV/Database
* Add proxy rotation to avoid blocking
* Improve error handling

---

##  Author

Shivam Malvankar

---

##  Acknowledgements

Inspired by real-world automation and web scraping use cases.
