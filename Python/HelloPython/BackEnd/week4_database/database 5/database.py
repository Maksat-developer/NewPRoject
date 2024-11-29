import psycopg2
from pprint import pprint as pp



postgres = psycopg2.connect(
    dbname='market', 
    user='batya', 
    password='123', 
    host='localhost'
)

cursor = postgres.cursor()


#cursor.execute('SELECT product_name,COUNT(product_name) FROM globus GROUP BY globus.product_id;')
# cursor.execute("SELECT product_name,day_to_expire FROM narodnii GROUP BY narodnii.product_id HAVING day_to_expire > 2;")
# cursor.execute("select sum(product_amount) from narodnii where product_name ='Snikers' AND product_amount != (select sum(product_amount)from globus where product_name = 'Snikers');")
#cursor.execute("SELECT product_name,product_name  FROM globus,narodnii WHERE product_name == day_to_expire ;")
#cursor.execute("SELECT * FROM globus INNER JOIN narodnii ON globus.product_type_id = globus.day_to_expire AND narodnii.product_type_id = narodnii.day_to_expire;")
# cursor.execute("SELECT * FROM globus WHERE product_name LIKE '%a' OR product_name LIKE '%b' OR product_name LIKE '%c' OR product_name LIKE '%d' OR product_name '%e' OR product_name LIKE '%f' OR product_name LIKE '%g' OR product_name LIKE '%a';")
#cursor.execute("SELECT * FROM globus INNER JOIN narodnii ON globus.day_to_expire = globus.day_to_expire AND narodnii.day_to_expire = narodnii.day_to_expire;")
# cursor.execute("SELECT product_amount,product_name FROM narodnii WHERE product_amount = ('SELECT * FROM narodnii WHERE product_amount < 200');")
# cursor.execute("SELECT * FROM globus INNER JOIN narodnii ON narodnii.date_delivered AND globus.date_delivered")

postgres.commit

record = cursor.fetchall()
pp(record)