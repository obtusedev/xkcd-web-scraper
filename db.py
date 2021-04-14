import sqlite3


# cursor.execute("""CREATE TABLE IF NOT EXISTS xkcd (title TEXT NOT NULL PRIMARY KEY, url TEXT, file_path TEXT)""")


def check_if_entry_exist(**kwargs):
    if kwargs["title"] is not None:
        connection = sqlite3.connect("xckd.db")
        cursor = connection.cursor()
        title_to_check = kwargs["title"]
        check_query = cursor.execute("SELECT * FROM xkcd WHERE title=(?)", (title_to_check,))
        does_exist = check_query.fetchone()
        if does_exist is not None:
            return True
        else:
            return False


def insert_comic_data(**kwargs):
    connection = sqlite3.connect("xckd.db")
    cursor = connection.cursor()
    kwargs.setdefault("url", "none")
    kwargs.setdefault("path_to_file", "none")
    title = kwargs["title"]
    url = kwargs["url"]
    path_to_file = kwargs["path_to_file"]
    if check_if_entry_exist(title=title):
        print(f"The entry {title} already exists.")
        pass
    else:
        cursor.execute("INSERT INTO xkcd VALUES (?, ?, ?)", (title, url, path_to_file))
        connection.commit()  # save changes
        connection.close()
