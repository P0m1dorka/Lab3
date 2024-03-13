# This is a sample Python scri
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import psycopg2
from Databaz import Databaze
user=input("Type name to connect")
user_password=input("Type bd password")
bd_connect = Databaze(user_password,user)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#conn = psycopg2.connect(database=bd_name, user=user, password=user_password, host="127.0.0.1", port="5432")
#cursor = conn.cursor()

