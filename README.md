# apt-price-checker
A Python web-scraping script, which exports results to CSV format. 

## Dependencies
- Python 3
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  - A Python library for pulling data out of HTML and XML files.
  - Install: `pip install beautifulsoup4`

## Usage 
`python3 apartment-price-checker.py`

## CSV Notes
* **CLOSE THE CSV**. The program will not append results to the .csv file if it is open on your system.
* The program will create the file if it does not exist. 
* The program will save the .csv file to the same directory the script is located at. 

## Other Notes
* This is not intended for use with any site other than the one that is hardcoded.
* If the hardcoded site is updated, this program may no longer work. 
