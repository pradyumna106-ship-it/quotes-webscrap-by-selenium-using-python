# Quotes Web Scraper using Selenium

A Python-based web scraper that uses Selenium to automatically log into a website and extract famous quotes with their authors, saving them to a CSV file.

## 📋 Overview

This project demonstrates web automation and scraping using **Selenium WebDriver** to:
- Automate browser login to a website
- Extract quotes and author information from the web page
- Store the data in a CSV file for further analysis

## 🎯 Features

- **Automated Login**: Uses Selenium to fill login credentials and submit the form
- **Quote Extraction**: Finds and extracts all quotes and their corresponding authors from the page
- **Data Processing**: Cleans up quote text (removes surrounding quotes)
- **CSV Export**: Exports the scraped data to `quote.csv` for easy access

## 📦 Dependencies

- **selenium**: Web automation tool for browser control
- **pandas**: Data manipulation and CSV export

Install dependencies using:

```bash
pip install selenium pandas
```

You'll also need to download **ChromeDriver** matching your Chrome browser version from [chromedriver.chromium.org](https://chromedriver.chromium.org)

## 🚀 Usage

Run the script directly:

```bash
python automation.py
```

### Script Workflow:

1. Opens Chrome browser
2. Navigates to `https://quotes.toscrape.com/login`
3. Finds and fills login fields with credentials:
   - Username: `username`
   - Password: `password123`
4. Clicks the login button
5. Extracts all quotes and authors from the page
6. Cleans the quote text (removes leading/trailing quotes)
7. Creates a DataFrame with Author and Quote columns
8. Exports data to `quote.csv`
9. Closes the browser

## 📊 Output

The script generates a `quote.csv` file with the following structure:

| Author | Quote |
|--------|-------|
| Albert Einstein | The world as we have created it is a process of our thinking... |
| J.K. Rowling | It is our choices, Harry, that show what we truly are... |
| ... | ... |

## 🔑 Key Methods Used

- `webdriver.Chrome()`: Initialize Chrome browser
- `driver.implicitly_wait()`: Set implicit wait time
- `driver.find_element()`: Locate elements by ID, Class, XPath
- `element.send_keys()`: Input text into form fields
- `element.click()`: Click on elements
- `pd.DataFrame()`: Create data structure
- `df.to_csv()`: Export data to CSV file

## ⚙️ Configuration

**Note:** Update the credentials in the script before running:

```python
username.send_keys('your_username')
password.send_keys('your_password')
```

## 📝 Author

Created on: Sat Apr 11 17:34:34 2026  
Author: prady

## 📚 Related Resources

- [Selenium Documentation](https://www.selenium.dev/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Quotes Website](https://quotes.toscrape.com/)

## 🔧 Troubleshooting

- **ChromeDriver version mismatch**: Ensure ChromeDriver version matches your Chrome browser
- **Element not found**: Check if the website structure has changed and update selectors accordingly
- **Login failures**: Verify credentials and wait times are sufficient

## 📄 License

This project is open for educational and personal use.
