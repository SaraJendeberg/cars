# cars
Webserver built in python and Django using an sqlite-database. Assuming you have python3 and sqlite installed.

In order to initialize database, cd to directory /djangoproject on your computer, run the command:
>> sqlite3 car_db.sqlite < database_setup.sql

In order to start the server, run:
>> python3 manage.py runserver

If you get an error-message such as "No mode named <module_name>", run:
>> pip install <module_name>

Enjoy!
