# This is a sample Python scri
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import psycopg2
from Databaz import Databaze, AuthenticateExeption, AvtorizationExeption, InputExeption



baza = Databaze('5','5')
av = AvtorizationExeption()
au = AuthenticateExeption()
ie = InputExeption()
av.set_next(au)
au.set_next(ie)
print(av.throw_exeption(baza))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#conn = psycopg2.connect(database=bd_name, user=user, password=user_password, host="127.0.0.1", port="5432")
#cursor = conn.cursor()

