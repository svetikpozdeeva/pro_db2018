from redis import Redis
import sqlite

"""
Исходная задача - есть БД, в качестве БД выступает SQLite база данных.
Источник данных - CSV файлы https://www.rossvyaz.ru/activity/num_resurs/registerNum/
Она хранит полями диапазоны телефонных номеров и привязку к регионам
https://www.rossvyaz.ru/activity/num_resurs/registerNum/
Реализовать на Redis промежуточный кэш для данных, срок жизни 2 секунды.
При выборке из кэша сообщать об этом.
Собрать статистику.
"""
