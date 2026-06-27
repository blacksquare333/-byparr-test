import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random


all_products = []

for page in range(1, 4):  
    print(f"正在爬第{page}页...")
    
    url = f"https://www.g2.com/categories/project-management?order=g2_score&page={page}#product-list"

    html = None
    for attempt in range(5):
    
        response = requests.post("http://localhost:8191/v1", json={
            "cmd": "request.get",
            "url": url,
            "maxTimeout": 60000
        })
    
        data = response.json()
        if data.get('status') == 'ok':
            html = data['solution']['response']
            break
        else:
            print(f"第{page}页第{attempt+1}次失败，FlareSolverr返回: {data}")
        
        time.sleep(random.uniform(5, 10))

    if not html:
        print(f"第{page}页3次都失败，跳过")
        continue
    
  
    soup = BeautifulSoup(html, 'html.parser')
    
    cards = soup.select('div.product-card__head')
    print(f"第{page}页找到{len(cards)}个产品")
    
    for card in cards:
        name = card.select_one('div.product-card__product-name')
        reviews = card.select_one('span.pl-4th')
        rating = card.select_one('span.fw-semibold')
        
        product = {
            'name': name.text.strip() if name else '',
            'reviews': reviews.text.strip() if reviews else '',
            'rating': rating.text.strip() if rating else ''
        }
        if product['name']:
            all_products.append(product)
    time.sleep(random.uniform(3, 6))        

df = pd.DataFrame(all_products)
df.to_excel('g2_products.xlsx', index=False)
print(f"总计导出{len(all_products)}条数据")