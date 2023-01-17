# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import datetime as dt
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    RESULT_COUNT = defaultdict(int)

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):

        self.RESULT_COUNT[item['status']] += 1
        return item

    def close_spider(self, spider):

        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        total = sum(self.RESULT_COUNT.values())
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        print('я тут')
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for value, key in self.RESULT_COUNT.items():
                f.write(f'{value},{key}\n')
            f.write(f'Total,{total}\n')
