import time
import requests
from bs4 import BeautifulSoup
from dict_of_file import dict_month


# การดึงหน้าเว็บส่วนข้อมูลทั้งหมด
def url_link():
    url = requests.get(
        "https://www.bot.or.th/thai/statistics/financialmarkets/_layouts/application/exchangerate/exchangerate.aspx")
    web = BeautifulSoup(url.content, "html.parser")
    all_web = web.find("div", {"id": "s4-workspace"})
    return all_web


# หัวข้อ บรรทัดที่ 1
def title1():
    title = url_link().find_all("div", {"class": "col-md-6 col-xs-12"})[0].text
    return title.strip()


# หัวข้อ บรรทัดที่ 2
def title_page1():
    title_1 = url_link().find_all("div", {"class": "col-md-6 col-xs-12"})[1].text
    return title_1.strip()


def title2(i):
    title_2 = url_link().find_all("div", {"class": "bot-rteElement-H1"})[i].text
    return title_2.strip()


def description_1():
    url = title2(0)
    list_url = url.split()
    b = (list_url[1][:len(list_url[1]) - 1] + " " + list_url[1][len(list_url[1]) - 1]).split()
    del list_url[1]

    list_url.insert(1, b[0])
    list_url.insert(2, b[1])

    c = ' '.join(list_url[3:7])
    del list_url[3:7]
    list_url.insert(3, c)

    d = ''.join(list_url[2:])
    list_url.insert(2, d)
    del list_url[3:]
    return list_url


# วันที่ Update ราคาล่าสุดที่อยู่บน Website
def update():
    now_time = []
    up = title1().split()
    for i in up:
        if i.isdigit():
            now_time.append(int(i))
        if i in dict_month:
            now_time.append(dict_month[i])
    return now_time


if __name__ == "__main__":
    print(update())
    print(time.process_time())
