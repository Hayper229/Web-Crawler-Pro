import requests
import bs4
import user_agent
import urllib3
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # без warning
links = []
tags = []
tg = []

def main(url):
    agent = f'{user_agent.generate_user_agent()}'
    headers = {'User-Agent': f'{agent}'}
    print(f'Selected User-Agent: {agent}')
    try:
       resp = requests.get(url=url, headers=headers, verify=False, timeout=10)
       soup = bs4.BeautifulSoup(resp.text, 'html.parser')
       for tag in soup.find_all(['a', 'img']):
           link = tag.get('href')
           if link and link.startswith('https://t.me/'):
              if link not in tg:
                 tg.append(link)
                 pass
           if link and link.startswith('http') and not link.startswith("https://t.me/") and not link.startswith('http://mailto:'):
              if link not in links:
                 links.append(link)
                 pass
       for link in links:
           print(f'Crawl lvl 1: {link}')
           resp = requests.get(url=link, headers=headers, verify=False, timeout=10)
           soup = bs4.BeautifulSoup(resp.text, 'html.parser')
           for tag in soup.find_all(['a', 'img']):
               link = tag.get('href')
               if link and link.startswith('https://t.me/'):
                  if link not in tg:
                     tg.append(link)
                     pass
               if link and link.startswith('http') and not link.startswith('https://t.me/') and not link.startswith('http://mailto:'):
                  if link not in links:
                     links.append(link)
                     pass
           for link in links:
               print(f'Crawl lvl 2: {link}')
               pass
           for tg_acc in tg:
               print(f'TG: {tg_acc}')

    except:
          pass

if __name__ == "__main__":
  url = input('URL: ')
   main(url)
