from scrapy.exceptions import DropItem

class DuplicatesPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item.__class__.__name__ == 'NewsItem':
            if item['url'] in self.ids_seen:
                raise DropItem("Duplicate item found: %s" % item)
            else:
                self.ids_seen.add(item['url'])
                return item
