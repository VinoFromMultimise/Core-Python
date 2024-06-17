import csv
import mysql.connector
import datetime
import sys

csv_data = csv.reader(open('employees.csv'))
header = next(csv_data)
print("Importing the file")

for row in csv_data:
	a = int(row[0])
	row[0] = a
	dt = row[1]
	dt_yr, dt_mn, dt_da = int(dt[6:]), int(dt[3:5]), int(dt[0:2])
	act_date = datetime.date(dt_yr, dt_mn, dt_da)	
	row[1] = act_date
	da = row[5]
	da_yr, da_mn, da_da = int(da[6:]), int(da[3:5]), int(da[0:2])
	act_date1 = datetime.date(da_yr, da_mn, da_da)	
	row[5] = act_date1
	r0 = tuple([row[0],row[1], row[2], row[3], row[4], row[5]])
	print(r0)
	mydb = mysql.connector.connect(
  			host="localhost",
  			user="root",
  			password="pass123",
  			database="emp_mm",autocommit = True
			)
	mycursor = mydb.cursor()
	mycursor.execute("INSERT INTO employees (emp_no,birth_date,first_name,last_name,gender,hire_date) VALUES(%s,%s,%s,%s,%s,%s)", r0, multi=True)
	#mycursor.commit
	mydb.commit
	mydb.close()

print(mycursor.rowcount, "record inserted.")
print("Done with insertion !!")
