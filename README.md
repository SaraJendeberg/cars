# cars
Webserver built in Python and Django using an sqlite-database. 

Assuming you have python3 and sqlite installed, in order to initialize database, cd to the directory where you downloaded the /car folder on your computer, run the command:
>> sqlite3 car_db.sqlite < database_setup.sql

In order to start the server, run:
>> python3 manage.py runserver

If you get an error-message such as "No module named <module_name>", run:
>> pip install <module_name>

The server sends responses in json format to
GET /employees: returns a list of all employees and their parameters
GET /carmodels: returns a list of all carmodels and their parameters
GET /total_sales: returns a list of all employees and their accumulated total sales
POST /carmodels: saves a new carmodel and returns it:
For example, sending POST /carmodels with the data
{
	"brand" : "TestBrand",
	"model" : "TestModel",
	"price" : "100000"
}
will return the same body back with the id that was added id. 

