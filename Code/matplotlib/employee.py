import csv
import matplotlib.pyplot as plt

data = [
    ["ID", "Name", "Department", "Salary"],
    [1, "Alice", "HR", 40000],
    [2, "Bob", "IT", 60000],
    [3, "Charlie", "Finance", 50000],
    [4, "David", "IT", 70000],
    [5, "Eve", "HR", 45000]
]

with open("employees.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

ids = []
names = []
departments = []
salaries = []

with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        ids.append(int(row["ID"]))
        names.append(row["Name"])
        departments.append(row["Department"])
        salaries.append(int(row["Salary"]))

plt.figure()
plt.bar(names, salaries)
plt.title("Employee Salaries")
plt.xlabel("Employees")
plt.ylabel("Salary")
plt.show()

dept_count = {}
for dept in departments:
    dept_count[dept] = dept_count.get(dept, 0) + 1

plt.figure()
plt.pie(dept_count.values(), labels=dept_count.keys(), autopct="%1.1f%%")
plt.title("Department Distribution")
plt.show()