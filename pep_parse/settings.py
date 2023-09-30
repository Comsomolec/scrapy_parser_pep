from pathlib import Path

BOT_NAME = "pep_parse"

SPIDER_MODULES = ["pep_parse.spiders"]

ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

BASE_DIR = Path(__file__).parent
RESULTS = 'results'
DOMAIN = 'peps.python.org'
STATUS_SUMMARY_FILENAME = 'status_summary_{current_time}.csv'

TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

FEEDS = {
    f'{RESULTS}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
