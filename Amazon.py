import requests
import re
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as t
import json
from selenium.webdriver.common.by import By
from playsound import playsound
from selenium.webdriver.chrome.options import Options


keywords_used = ["Hp laptop "]
targeted_email = "review"


def write_to_file(data):
    file_name = "data\data6.json"

    """
    try:
        with open('data.json','r',encoding='utf-8') as f:
            existing_list=json.load(f)
        existing_list.append(data)

        with open('data.json','w',encoding='utf-8') as f:
            json.dump(existing_list,f,indent=4)
    except UnboundLocalError:
        with open('data.json','w',encoding='utf-8') as f:
            json.dump(data,f,indent=4)"""

    try:
        with open("amazon.json", "r", encoding="utf-8") as f:
            existing_list = json.load(f)
        existing_list.extend(data)
        if len(existing_list) > 0:
            with open("amazon.json", "w", encoding="utf-8") as f:
                json.dump(existing_list, f, indent=4, separators=(",", ":"))
        else:
            with open("amazon.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, separators=(",", ":"))
    except FileNotFoundError:
        with open("amazon.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, separators=(",", ":"))


def extract_all(url):
    data = []
    # url=driver.current_url
    driver.get(url)
    t.sleep(10)
    html = driver.page_source
    soup = bs(html, "html.parser")
    all_divs = soup.find_all("div", {"class": "MjjYud"})
    print(len(all_divs))

    for i in all_divs:
        try:
            name = i.find("h3").text
            print(name)
            # username=i.find('div',{'class':'byrV5b'}).find('span').text
            # username = i.find("div", {"class": "byrV5b"}).find("span").text
            # username=str(username).split('›')[0].strip()
            # print(username)
            review = i.find(
                "div", {"class": "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf"}
            ).text
            # mail = re.findall(r"\w+@{}\.com".format(targeted_email), bio)
            print(review)
            d = {"name": name, "review": review}
            data.append(d)
        except Exception as e:
            print(e)
    write_to_file(data=data)


"""

PROXY="65.109.12.77:8080"
chrome_options = webdriver.ChromeOptions()
        
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')

chrome_options.add_argument('--proxy-server=%s' % PROXY)"""


url5 = "https://www.google.com/search?q=%22hp+laptop%22++%22reviews+%22+site:amazon.com&sxsrf=APwXEdfrq7OLq7WqSE4A_BXdoGVRmyIwaw:1684957153096&ei=4WduZJvLBYq6seMP4JKuSA&start=0&sa=N&ved=2ahUKEwjbv8nE2o7_AhUKXWwGHWCJCwk4HhDy0wN6BAgFEAQ&biw=1536&bih=792&dpr=1.25"
driver = webdriver.Chrome()
# driver.maximize_window()
driver.get(url5)

t.sleep(30)
html = driver.page_source
# print(html)
soup = bs(html, "html.parser")

all_divs = soup.find_all("div", {"class": "MjjYud"})
print(len(all_divs))

data = []  # stores data before writing

for i in all_divs:
    try:
        name = i.find("h3").text
        print(name)
        # username=i.find('div',{'class':'byrV5b'}).find('span').text
        # username = i.find("div", {"class": "byrV5b"}).find("span").text
        # username=str(username).split('›')[0].strip()
        # print(username)
        review = i.find(
            "div", {"class": "VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf"}
        ).text
        # mail = re.findall(r"\w+@{}\.com".format(targeted_email), bio)
        print(review)
        d = {"name": name, "review": review}
        data.append(d)
    except Exception as e:
        print(e)
write_to_file(data=data)

i = 1
while i == 1:
    try:
        next_pg = driver.find_element(By.PARTIAL_LINK_TEXT, "Next")
        next_pg.click()
        url = driver.current_url
        extract_all(url)
        t.sleep(10)
    except Exception as e:
        print("ERROR OCCURED!")
        # playsound('./sounds/alert_tones.mp3')
        t.sleep(10)
        ip = input("Enter y to quit an n to not ?  = > :")
        if ip == "y":
            break
    print(driver.current_url)


t.sleep(2)
print("all done")
driver.close()
driver.quit()
