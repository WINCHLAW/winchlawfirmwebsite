from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
import json
root=Path(__file__).resolve().parents[1]/'public'; count=0
for f in root.rglob('*.html'):
 s=BeautifulSoup(f.read_text(),'html.parser');count+=1
 assert s.find('h1'),f'{f}: missing h1'
 assert s.find('main'),f'{f}: missing main'
 canonical=s.find('link',rel='canonical')['href'];assert canonical.startswith('https://winchlawfirm.com')
 assert s.find('meta',property='og:url')['content']==canonical
 for name,attrs in [('og:image',{'property':'og:image'}),('twitter:image',{'name':'twitter:image'})]:assert s.find('meta',attrs=attrs)['content'].startswith('https://winchlawfirm.com/assets/')
 assert '504-377-2620' in s.get_text() and '504-500-1899' in s.get_text()
 for e in s.find_all(['a','img','script','link']):
  u=e.get('href') or e.get('src') or ''
  assert not u.startswith('http:'),f'{f}: insecure link {u}'
  if not u.startswith('/') or u.startswith('//'):continue
  path=urlsplit(u).path;target=root/path.lstrip('/')
  assert target.is_file() or (target/'index.html').is_file(),f'{f}: missing {path}'
 contact= s.find('form')
 if contact:
  assert contact.get('data-netlify')=='true';assert contact.find('input',{'name':'form-name'})['value']=='consultation'
  assert contact.get('enctype')=='multipart/form-data';assert contact.find('input',{'name':'document','type':'file'})
assert (root/'robots.txt').is_file() and (root/'sitemap.xml').is_file()
assert 'thank-you' not in (root/'sitemap.xml').read_text()
for slug in ['received-utility-right-of-way-offer-letter-louisiana','should-i-sign-utility-servitude-agreement-louisiana']:
 s=BeautifulSoup((root/'post'/slug/'index.html').read_text(),'html.parser');assert len(s.find('main').get_text())>6000
 if slug=='should-i-sign-utility-servitude-agreement-louisiana':
  records=[json.loads(tag.string) for tag in s.find_all('script',type='application/ld+json')]
  articles=[record for record in records if record.get('@type')=='Article']
  assert len(articles)==1,'Utility-servitude guide must retain exactly one Article schema after rebuild'
  schema=articles[0];canonical=s.find('link',rel='canonical')['href']
  assert schema['@context']=='https://schema.org'
  assert schema['@id']==canonical+'#article'
  assert schema['mainEntityOfPage']['@id']==canonical
  assert schema['headline']==s.find('h1').get_text(strip=True)
  assert schema['image']==s.find('meta',property='og:image')['content']
  assert schema['author']['name']=='Winch Law Firm, LLC'
print(f'PASS: {count} HTML documents; internal routes/assets, HTTPS links, metadata, both phone lines, form structure, retained articles, crawl files.')
