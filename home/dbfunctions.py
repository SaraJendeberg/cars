from django.db import connection
import sqlite3
import json

connection.row_factory = sqlite3.Row  # This enables column access by name: row['column_name']
c = connection.cursor()
'''
returns employee info
'''
def getEmployees():
    query = "SELECT * FROM employees"
    rows = c.execute(query)
    data = []
    for row in rows:
        data.append({'id': row[0], "name": row[1]})
    return data

'''
returns carmodel info
'''
def getCarModels():
    query = "SELECT * FROM carmodels"
    rows = c.execute(query)
    data = []
    for row in rows:
        data.append({'id': row[0], 'brand': row[1], 'model': row[2], 'price':row[3]})
    return data

'''
Add new car model to database
'''
def addNewCarModel(brand, model, price):
    query1 = "SELECT * FROM carmodels WHERE brand=\"%s\" and model=\"%s\" and price=%d" % (brand, model, price)
    c.execute(query1)
    res=c.fetchone() #returns None if no value passes
    if res is None: # if there isn't already a car of that brand, model and price
        try:
            query2 = "INSERT INTO carmodels(id, brand, model, price) VALUES(NULL, \"%s\", \"%s\", %d)" %(brand, model, price)
            c.execute(query2)
            query3 = "SELECT * FROM carmodels WHERE id = %d" % (c.lastrowid)
            rows = c.execute(query3)
            connection.commit()  # save
            data = []
            for row in rows:
                data.append({'id': row[0], 'brand': row[1], 'model': row[2], 'price': row[3]})
            return data
        except connection.Error:
            c.rollback()
    else:
        return "That car brand, model and price is already in the database. Try adding another brand, model and price."

'''
Returns attributes of all employees including total sales pricing
'''
def getTotalSales():
    query = "SELECT e.id, e.name, SUM(c.price) AS total_sales FROM(sales AS s INNER JOIN employees AS e ON s.employee_id = e.id INNER JOIN carmodels AS c ON s.carmodel_id = c.id) GROUP BY (e.id)"
    rows = c.execute(query)
    data = []
    for row in rows:
        data.append({'id': row[0], 'name': row[1], 'total_sales': row[2]})
    return data
