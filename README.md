# xkcd Comic Web Scraper

## About
This web scraper scrapes the [xkcd](https://xkcd.com/)
site and returns the comic title, direct url.
It then stores it along with the image location in an [SQLite3](https://www.sqlite.org/index.html) db.
This project was done to learn web scraping and sql/database.

## How to use
**Note** this project uses Python 3.8.5  
run `$ python main.py` or  
run `$ python3 main.py`

## Screenshots
First time running the program  
![first time you run the program](https://i.imgur.com/DNX6Rlf.png)  
If the images already exist in the db  
![second time running the program](https://i.imgur.com/kclAcLD.png)

## Libraries used
* Requests
* BeautifulSoup4
* Black
