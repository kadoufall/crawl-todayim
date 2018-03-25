import pymysql


class MySQLPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='115.28.169.114',
            db='todayim',
            user='kadoufall',
            passwd='123456',
            charset='utf8',
            use_unicode=False)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "insert ignore into news(url, loc, title, postTime, commentNum, viewNum, className, passageContent) VALUES(%s, %s, %s, %s, %s, %s, %s, %s);"
        params = (item['url'], item['loc'], item['title'], item['postTime'],
                  item['commentNum'], item['viewNum'], item['className'], item['passageContent'])
        self.cursor.execute(sql, params)
        self.conn.commit()
        return item
