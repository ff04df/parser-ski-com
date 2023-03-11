import config

import requests

from bs4 import BeautifulSoup

from openpyxl import Workbook

import asyncio
import aiohttp


async def productsHandler(products, ws):
    def valueFromString(s : str) -> str:
        wasDec = False
        start, end = 0, 0
        for en, i in enumerate(s):
            if not wasDec and i.isdecimal():
                start = en
                wasDec = True
                continue
            elif wasDec and (not i.isdecimal() and not i == ','):
                end = en
                break
        return s[start:end].replace(',', '.') if end != 0 else '0'
    
    async def productsHandlerAdditional(product):
        title = product.find('div', class_ = 'product__title').next.lstrip('\n ').rstrip('\n ')
        urlProd = 'https://www.cki-com.ru%s' % product['href']
        
        info = ''
        try:
            info = product.find('div', class_ = 'product__min-text').text.lstrip('\n ').rstrip('\n ')
        except: pass
        
        modificationsCount = int(valueFromString(product.find('li', class_ = 'product__list-item').text.lstrip('\n ').rstrip('\n ')))
        minPrice = float(valueFromString(product.find('li', class_ = 'product__list-item--price').text.lstrip('\n ').rstrip('\n ')))
        description = ''
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url=urlProd, headers=config.HEADERS) as reqProduct:
                if reqProduct.status == 200:
                    try:
                        bsProd = BeautifulSoup(await reqProduct.read(), 'html.parser')
                        description = bsProd.find('div', class_ = 'item__desc').text.lstrip('\n ').rstrip('\n ') # type: ignore
                    except: pass
        
        ws.append([title, info, description, modificationsCount, minPrice, urlProd])
    
    await asyncio.gather(*[productsHandlerAdditional(product) for product in products])
        
        


class parser:
    def start(self):
        session = requests.Session()
        
        wb = Workbook()
        
        ws = wb.active
        ws.append(['Название', 'Информация', 'Описание', 'Кол-во модификаций', 'Минимальная цена', 'Ссылка']) # type: ignore
        
        if config.CREATE_SHEETS:
            wb.remove(wb.active) # type: ignore
        
        for url in config.URLS:
            if config.CREATE_SHEETS:
                tit = BeautifulSoup(session.get(url=url, headers=config.HEADERS).content,
                                    'html.parser').find('h1', class_='t-h1').text.lstrip('\n ').rstrip('\n ') # type: ignore
                if len(tit) > 31:
                    tit = tit[:31]
                ws = wb.create_sheet(tit)
                
                ws.append(['Название', 'Информация', 'Описание', 'Кол-во модификаций', 'Минимальная цена', 'Ссылка'])
            
            for i in range(1, config.MAX_PAGES + 1):
                req = session.get(url=f'{url}?PAGEN_1={i}', headers=config.HEADERS)
                if req.status_code != 200:
                    print(f'{url}?PAGEN_1={i}\ncode: {req.status_code}')
                    break
                
                bs = BeautifulSoup(req.content, 'html.parser')
                
                try:
                    if str(i) != bs.select_one('div.pagination__page.is-active').text: # type: ignore
                        break
                except:
                    asyncio.run(productsHandler(bs.find_all('a', class_ = 'product'), ws))
                    break
                asyncio.run(productsHandler(bs.find_all('a', class_ = 'product'), ws))
                
                
        wb.save(config.EXCEL_FILENAME)
        print(f'\nSaved excel file with name: {config.EXCEL_FILENAME}')
