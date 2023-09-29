import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).parent
RESULTS = 'results'
TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
STATUS_SUMMARY_FILENAME = 'status_summary_{current_time}.csv'


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.count_pep_status = defaultdict(int)

    def process_item(self, item, spider):
        self.count_pep_status[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        now_formatted = datetime.now().strftime(TIME_FORMAT)
        file_name = STATUS_SUMMARY_FILENAME.format(current_time=now_formatted) 
        file_path = self.results_dir / file_name 
        with open(file_path, 'w', encoding='utf-8', newline='') as file: 
            csv.writer(file, dialect=csv.unix_dialect).writerows([
                ('Статус, Количество', ),
                self.count_pep_status.items(),
                ('Всего', sum(self.count_pep_status.values()))
            ])
