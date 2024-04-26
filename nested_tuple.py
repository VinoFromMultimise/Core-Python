# Nested sequence (tuple) and dictionary in the list

employees = [
     ("Sanmaya", 20, "Software Engineer"),
     ("Aadhi", 25, "Web Developer"),
     ("Gayathri", 23, "Data Analyst"),
     ("Mark Antony", 22, "Intern"),
     ("Subramani", 30, "Project Manager")
 ]

#To access Gayathri's record - Get Gayathri's role
print('Gayathri', "'s", 'role in Multimise: ', employees[2][2])

# To access subramani's record - Use negative indexing
print('Subramani',"'s", 'role in Multimise: ', employees[-1][-1])

#Traversing the nested sequence in the list
for name, age, role in employees:
    print('Name = ',name, ', Age = ', age, ', Role = ', role)

# Dict inside the List
employees = [
     {"name": "Sanmaya", "age": 30, "job": "Software Engineer"},
     {"name": "Aadhi", "age": 25, "job": "Web Developer"},
     {"name": "Gayathri", "age": 45, "job": "Data Analyst"},
     {"name": "Mark Antony", "age": 22, "job": "Intern"},
     {"name": "Subramani", "age": 36, "job": "Project Manager"}
]

# Try to access Mark's record

print(employees[3]["name"])
print(employees[3]["age"])
print(employees[3]["job"])
