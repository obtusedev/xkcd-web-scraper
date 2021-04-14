import os
import requests
from bs4 import BeautifulSoup
from db import insert_comic_data

num = 1
while num < 6:
    print(f"Scraping...{num}")
    url = f"https://xkcd.com/{num}/"

    res = requests.get(url)
    content = res.text
    soup = BeautifulSoup(content, "html.parser")

    comic_title = soup.find(id="ctitle").text
    partial_link = soup.find(id="comic").find("img")["src"]
    img_link = "https:" + partial_link

    img = requests.get(img_link).content

    # check if folder img exists
    if os.path.exists(os.getcwd() + "\\img"):
        with open(
            f"{os.path.abspath('img')}/{str(num)}) {comic_title}.jpg", "w+b"
        ) as f:
            f.write(img)
    else:
        os.mkdir(os.getcwd() + "\\img")
        with open(
            f"{os.path.abspath('img')}/{str(num)}) {comic_title}.jpg", "w+b"
        ) as f:
            f.write(img)

    file_path = f'{os.path.abspath("img")}\\{str(num)}) {comic_title}.jpg'

    insert_comic_data(title=comic_title, url=img_link, path_to_file=file_path)

    num += 1

print("Done")

"""
1) Go through a x number of xkcd comics
2) Get the title, img_url, and download the actual img
3) Input into SQLite3 DB title, img_url, and link to img
4) Make dir for all the img
@@@ TODO
1) Download files to img dir
2) Find way to get path to img; maybe os.path.abspath()
3) Insert the data into db
4) Add progress indicator
5) Make img folder/dir if it does not exist
"""
