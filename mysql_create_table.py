import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass123",
  database="emp_mm"
)

mycursor = mydb.cursor()

sql_employees = "CREATE TABLE employees (emp_no INT NOT NULL,birth_date DATE NOT NULL,first_name  VARCHAR(14) NOT NULL,last_name VARCHAR(16) NOT NULL,gender ENUM ('M','F')  NOT NULL,hire_date DATE NOT NULL,PRIMARY KEY (emp_no));"

mycursor.execute(sql_employees)

sql_dept = "CREATE TABLE departments (dept_no CHAR(4) NOT NULL, dept_name VARCHAR(40) NOT NULL, PRIMARY KEY (dept_no), UNIQUE  KEY (dept_name));"

mycursor.execute(sql_dept)

sql_dep_emp = "CREATE TABLE dept_emp (emp_no INT NOT NULL,dept_no CHAR(4) NOT NULL,from_date DATE NOT NULL,to_date DATE NOT NULL,KEY (emp_no),KEY (dept_no),FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE, FOREIGN KEY (dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE,PRIMARY KEY (emp_no, dept_no));"

mycursor.execute(sql_dep_emp)

mycursor.execute("show tables")