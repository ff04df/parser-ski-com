HEADERS = {'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; rv:110.0) Gecko/20100101 Firefox/110.0'}

# urls to parse

URLS = [
    'https://www.cki-com.ru/catalog/fasteners/bolts_screws/',
    'https://www.cki-com.ru/catalog/fasteners/nuts/',
    'https://www.cki-com.ru/catalog/fasteners/screws/',
    'https://www.cki-com.ru/catalog/fasteners/shims_rings/',
    'https://www.cki-com.ru/catalog/fasteners/pins_cotters/',
    
    'https://www.cki-com.ru/catalog/fasteners/anchor_dowels/',
    'https://www.cki-com.ru/catalog/fasteners/tackle/',
    'https://www.cki-com.ru/catalog/fasteners/mounts/',
    'https://www.cki-com.ru/catalog/fasteners/furniturefittings/',
    'https://www.cki-com.ru/catalog/fasteners/nails/',
    
    'https://www.cki-com.ru/catalog/fasteners/press/',
    'https://www.cki-com.ru/catalog/fasteners/security/',
    'https://www.cki-com.ru/catalog/fasteners/anaerobic/',
    'https://www.cki-com.ru/catalog/fasteners/racks/',
    'https://www.cki-com.ru/catalog/fasteners/vysokoprochnyy-krepezh/',
]

# max pages to parse
# * should be 10

MAX_PAGES = 10

# name of excel file to save

EXCEL_FILENAME = 'pr.xlsx'

# whether create sheets with name like: "Болты, винты, шпильки"
# If false, it stores all information in first sheet

CREATE_SHEETS = True
