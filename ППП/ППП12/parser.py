import requests as rqs
from bs4 import BeautifulSoup
import re


#  YANDEX
def get_res_ya(url, headers):
    while True:
        res = rqs.get(url, headers=headers)
        if res.status_code == 200 and not "http://ogp.me/ns#" in BeautifulSoup(res.text, "html.parser"):
            return res.text
        else:
            return None


def parse_catalog_ya(res, base_url):
    soup = BeautifulSoup(res, "html.parser")
    links = soup.find_all("a", {"class": "place-list__item-name"})
    links_lst = []
    for link in links:
        links_lst.append(base_url + link.get("href"))
    return links_lst


def get_city_name_ya(url):
    return re.search(r"a/(.+)\?", url)[1]


def parse_website_ya(res):
    soup = BeautifulSoup(res, "html.parser")
    forecast = soup.find_all("a", {"class": "forecast-briefly__day-link"})

    lst_forecast = []
    for i in forecast[1:9]:
        lst_forecast.append(i.get("aria-label").split(",")[1:4])

    day_f = ["Error"]
    week_f = []
    for day in lst_forecast:
        day_f = []
        ind_d = re.search(r"\d{1,2}", day[0])
        ind_t = re.search(r"(-\d{1,2}|\d{1,2})", day[2])
        day_f = [ind_d[0], int(ind_t[0]), day[1].strip(" ")]
        week_f.append(day_f)

    return week_f


def get_data_ya(base_url, url, headers):
    res = get_res_ya(url, headers)
    while True:
        if res:
            links_lst = parse_catalog_ya(res, base_url)
            break

    links_cities = []
    for link in links_lst:
        res = get_res_ya(link, headers)
        if not "sun-card__sun-circles" in BeautifulSoup(res, "html.parser") and res:
            links_cities += parse_catalog_ya(res, base_url)
        else:
            links_cities.append(link)
        if len(links_cities) >= 1000:
            links_cities = links_cities[:1000]
            break

    dct_data = {}
    for site in links_cities:
        res = get_res_ya(site, headers)
        if res:
            week_f = parse_website_ya(res)
            city_name = get_city_name_ya(site)
            dct_data[city_name] = week_f

    return dct_data


#  RAMBLER
def get_res_ra(url, headers):
    while True:
        res = rqs.get(url, headers=headers)
        if res.status_code == 200:
            return res.text
        else:
            return None


def parse_catalog_ra(res, base_url, href_class):
    soup = BeautifulSoup(res, "html.parser")
    links = soup.find_all("a", {"class": href_class})
    links_lst = []
    for link in links:
        links_lst.append(base_url + link.get("href"))
    return links_lst


def get_city_name_ra(url):
    city_name = re.search(r"ru/(.+)/10", url)[1]
    if "/" in city_name:
        return re.search(r"(.+)/(.+)")[1]
    else:
        return city_name


def parse_website_ra(res):
    soup = BeautifulSoup(res, "html.parser")
    forecast = soup.find_all("div", {"class": ["NMb4", "TBhb"]})

    lst_forecast = []
    day_f = ["Error"]
    week_f = []
    for i in forecast[:8]:
        day = i.find("span", {"class": "xNwL"}).string
        day_t = i.find("span", {"class": "Njqa"}).text[:-1]
        day_c = i.find("svg", {"class": "zDgs"}).find("path").get("d")
        try:
            day_f = [int(day.split(" ")[0]), int(day_t), day_c]
        except ValueError:
            pass
        week_f.append(day_f)

    return week_f


def get_data_ra(base_url, url, headers):
    res = get_res_ra(url, headers)
    if res:
        links_lst = parse_catalog_ra(res, base_url, "kgSF")

    links_cities = []
    for link in links_lst:
        res = get_res_ra(link, headers)
        if "world" in link and res:
            links_cities += parse_catalog_ra(res, base_url, "MJZ5")
        else:
            links_cities.append(link)
        if len(links_cities) >= 1000:
            links_cities = links_cities[:1000]
            break
    links_cities_links = list(map(lambda x: x + "10-days/", links_cities))

    dct_data = {}
    for site in links_cities_links:
        res = get_res_ra(site, headers)
        if res:
            week_f = parse_website_ra(res)
            city_name = get_city_name_ra(site)
            dct_data[city_name] = week_f

    return dct_data


#  GISMETEO
def get_res_gi(url, headers):
    while True:
        res = rqs.get(url, headers=headers)
        if res.status_code == 200:
            return res.text
        else:
            return None


def parse_catalog_gi(res, base_url):
    soup = BeautifulSoup(res, "html.parser")
    soup_groups = soup.find("div", {"class": "groups"})
    links = soup_groups.find_all("a", {"class": "link-item"})
    links_lst = []
    for link in links:
        links_lst.append(base_url + link.get("href"))
    return links_lst


def get_city_name_gi(url):
    return re.search(r"weather-(.+)-\d+", url)[1]


def parse_website_gi(res):
    soup = BeautifulSoup(res, "html.parser")
    forecast_table = soup.find("div", {"class": "widget-items"})
    forecasts_days = forecast_table.find_all("div", {"class": "date"})

    forecasts_tmp = soup.find("div", {"class": "ten-days"}).find_all("div", {"class": "maxt"})

    forecasts_cl = forecast_table.find_all("div", {"class": ["weather-icon", "tooltip"]})

    day_f = ["Error"]
    week_f = []
    for i in range(7):
        day_f = []
        day = forecasts_days[i].string
        ind_d = re.search(r"\d{1,2}", day)
        day_f.append(int(ind_d[0]))
        tmp = re.search(r"(-\d{1,2}|\d{1,2})", forecasts_tmp[i].find("span", {"class": "unit_temperature_c"}).string)[0]
        print(tmp)
        day_f.append(int(tmp))
        cl = forecasts_cl[i].get("data-text")
        day_f.append(cl)
        week_f.append(day_f)

    return week_f


def get_data_gi(base_url, url, headers):
    res = get_res_gi(url, headers)
    if res:
        links_lst = parse_catalog_gi(res, base_url)

    links_cities_2 = []
    for link in links_lst:
        res = get_res_gi(link, headers)
        if res and "catalog" in link:
            links_cities_2 += parse_catalog_gi(res, base_url)
        elif "weather" in link:
            links_cities_2.append(link)
        if len(links_cities_2) >= 1000:
            links_cities_2 = links_cities_2[:1000]
            break

    links_cities = []
    for link in links_cities_2:
        res = get_res_gi(link, headers)
        if res and "catalog" in link:
            links_cities += parse_catalog_gi(res, base_url)
        elif "weather" in link:
            links_cities.append(link)
        if len(links_cities) >= 1000:
            links_cities = links_cities[:1000]
            break

    links_cities = list(map(lambda x: x + "10-days/", links_cities))

    dct_data = {}
    for site in links_cities:
        res = get_res_gi(site, headers)
        if res:
            week_f = parse_website_gi(res)
            city_name = get_city_name_gi(site)
            dct_data[city_name] = week_f

    return dct_data
