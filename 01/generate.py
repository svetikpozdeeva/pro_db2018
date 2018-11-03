from faker import Faker
import random

f = Faker("ru_RU")

users = [] #10 пользователей -> users.json, users.csv
products = [] #10 товаров -> products.json, products.csv
sales = [] #0-10 случайных продаж случайного товара каждому пользователю ->sales.json, sales.csv

user = {'name':"...", 'mail':"...", 'phone':"..."}
product = {'name':"...", 'price': random.randomint(10000) / 100}
sale = {'user':"name/id", 'product':"name/id", 'date':randomDate((2017,01,01),(2018,12,31)), 'count':random.randomint(10)} 
#https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
