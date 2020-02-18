from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl # 기숙사 페이지를 url_open할 때 [SSL: CERTIFICATE_VERIFY_FAILED]을 무시하기 위함

from datetime import datetime
import re
import sqlite3
import html
from menu.models import *


def meal_handler(kr_name, price, restaurant_name):
    restaurant = Restaurant.objects.get(kr_name=restaurant_name)
    Meal.objects.get_or_create(
        kr_name=kr_name,
        price=price,
        restaurant=restaurant
    )


def menu_handler(meals, date, restaurant_name, type):
    restaurant = RestauranSNUCOt.objects.get(kr_name=restaurant_name)
    menu = Menu.objects.get(date=date, restaurant=restaurant, type=type)
    # menu.meals.set(meals) #이전 식샤코드, set?
    menu.meals.add(meals)
    menu.save()


def crawl_snu():
    crawl_snuco()


def crawl_snuco():
    SNUCO = "http://snuco.snu.ac.kr/ko/foodmenu"
    SNUCO_html = urlopen(SNUCO).read()
    SNUCO_soup = BeautifulSoup(SNUCO_html, "html.parser")
    restaurant_list = []
    for restaurant in SNUCO_soup.find_all("td", class_="views-field-field-restaurant"):
        restaurant_list += re.findall('[0-9]*[ㄱ-ㅣ가-힇]+', restaurant.text)
    # print(restaurant_list)

    menu_text = SNUCO_soup.find_all("td", class_="views-field")
    re_menu_name = re.compile(r'([ㄱ-ㅣ가-힇a-zA-Z&()#;]*)\s+([0-9]{1,2},[0-9]{3})')
    restaurant = ""
    meals = []
    meal_types = {'breakfast': 'BR', 'lunch': 'LU', 'dinner': 'DN'}
    #print(menu_text)
    for menu_or_restaurant in menu_text:
        menu_or_restaurant_str = str(menu_or_restaurant)
        restaurant_or_none = re.search("[0-9]*[ㄱ-ㅣ가-힇]+", menu_or_restaurant_str)
        if restaurant_or_none:
            restaurant_or_none = restaurant_or_none.group()
        if restaurant_or_none in restaurant_list:
            restaurant = restaurant_or_none
            continue
        else:
            for meal_type in meal_types:
                if re.search(meal_type, menu_or_restaurant_str):
                    break  # 찾지 못하는 경우가 존재하나?
            v = re_menu_name.search(menu_or_restaurant_str)
            while v is not None:
                '''
                meal_name = v.group(1)
                price = int(re.sub(',', '', v.group(2)))
                meal_handler(meal_name, price, restaurant)
                meal = Meal.objects.get(kr_name = meal_name, restaurant= Restaurant.objects.get(kr_name=restaurant))
                meals.append(meal)
                menu_handler(meals, datetime.today(), restaurant, meal_types[meal_type])
                '''

                print(v.group(1), int(re.sub(',', '', v.group(2))), restaurant)
                menu_or_restaurant_str = re_menu_name.sub(' ', menu_or_restaurant_str, count=1)
                v = re_menu_name.search(menu_or_restaurant_str)

def crawl_dorm():
    dorm_url = "https://dorm.snu.ac.kr/dk_board/facility/food.php"
    context = ssl._create_unverified_context()#SSL 이슈
    dorm_html = urlopen(dorm_url, context= context).read()
    dorm_soup = BeautifulSoup(dorm_html, "html.parser")
    #아워홈, 919
