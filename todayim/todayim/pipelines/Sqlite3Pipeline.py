import sqlite3


class Sqlite3Pipeline(object):

    def __init__(self):
        self.sqlite_file = 'olderNews.db'
        self.sqlite_table = 'news'

    def open_spider(self, spider):
        self.conn = sqlite3.connect(self.sqlite_file)
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        sql = "insert or ignore into news(url, loc, title, postTime, commentNum, viewNum, className, passageContent) VALUES(?, ?, ?, ?, ?, ?, ?, ?);"
        params = (item['url'], item['loc'], item['title'], item['postTime'],
                  item['commentNum'], item['viewNum'], item['className'], item['passageContent'])
        self.cursor.execute(sql, params)
        self.conn.commit()
        return item
