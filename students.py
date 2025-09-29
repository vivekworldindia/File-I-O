# import csv

# students = []

# with open("students.csv" ,"r") as file:
#     reader = csv.DictReader(file)
#     for row  in reader:
#         students.append({"name":row["name"],"home":row["home"]})
        
#     # for line in file:
#     #     name , home,info = line.rstrip().split(",")
#     #     student = {"name":name,"home":home,"info":info}
#     #     students.append(student)
        
# # def get_name(student):
# #     return student["name"]

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

        
        
import csv 

name = input("what's your name? ")
home = input("where's your home ?")

with open("students.csv","a") as file:
    writer  = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name":name,"home":home})