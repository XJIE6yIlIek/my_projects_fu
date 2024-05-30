import requests as rqs
from fake_useragent import UserAgent

url = "https://yandex.ru/pogoda/region/225?via=moc"
user_agent = UserAgent()
headers = {"User-Agent": user_agent.random}
print(rqs.get(url, headers=headers).url)
