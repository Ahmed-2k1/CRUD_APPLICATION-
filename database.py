from flask import g
import sqlite3

def conncect_to_database():
    sql = sqlite3.connect('/Users/mohammedahmeduddinyasar/Documents/FLASK_CRUD_APPLICATION/venv/crudapplication.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_database():
    if not hasattr(g, 'crudapplication_db'):
        g.crudapplication_db = conncect_to_database()
    return g.crudapplication_db
