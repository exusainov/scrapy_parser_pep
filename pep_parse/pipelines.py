import csv
import datetime as dt
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:

    def open_spider(self, spider):
        self.RESULT_COUNT = defaultdict(int)

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
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow(['Статус', 'Количество'])
            for value, key in self.RESULT_COUNT.items():
                writer.writerow([value, key])
            writer.writerow(['Total', total])
