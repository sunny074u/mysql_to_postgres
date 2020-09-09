import mysql.connector as mc
from mysql.connector import errorcode as ec

user = "retail_user"
password = "#Abcd4321"
host = "localhost"
db = "retail"

try:
    connection = mc.connect(user=user,
                        host=host,
                        password=password,
                        database=db
                        )

    orders_cursor = connection.cursor()
    query = """SELECT * FROM orders LIMIT 10"""
    orders_cursor.execute(query)
    for order in orders_cursor:
        print(order)
except mc.Error as error:
    if error.error == ec.ER_ACCESS_DENIED_ERROR:
        print("Invalid Credentials")
    else:
        print(error)
else:
    connection.close()