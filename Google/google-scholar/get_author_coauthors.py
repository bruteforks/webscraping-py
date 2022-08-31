from bs4 import BeautifulSoup
import requests, lxml, os

headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

proxies = {
  'http': os.getenv('HTTP_PROXY')
}

def get_authors_co_authors():
  html = requests.get('https://scholar.google.com/citations?hl=en&user=m8dFEawAAAAJ', headers=headers, proxies=proxies).text

  soup = BeautifulSoup(html, 'lxml')

  try:
    for container in soup.select('.gsc_rsb_aa'):
      author_name = container.select_one('#gsc_rsb_co a').text
      author_affiliations = container.select_one('.gsc_rsb_a_ext').text
      author_link = container.select_one('#gsc_rsb_co a')['href']

      print('Co-Author(s):')
      print(f'{author_name}\n{author_affiliations}\nhttps://scholar.google.com{author_link}\n')
  except:
    pass
