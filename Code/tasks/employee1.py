import csv
import random
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

employees = []

choice = input("Enter '1' for auto-generate or '2' for manual input: ")

if choice == '2':
    n = int(input("How many employees do you want to enter (max 15): "))
    
    if n > 15:
        n = 15

    for i in range(n):
        print(f"\nEmployee {i+1}")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        salary = float(input("Enter salary: "))
        salary = salary + (salary * 0.05)
        employees.append([name, age, round(salary, 2)])

else:
    sample_names = ["John","Alice","Bob","David","Emma","Chris","Sophia","Daniel","Olivia","James","Liam","Mia","Noah","Ava","Ethan"]
    for i in range(15):
        name = sample_names[i]
        age = random.randint(21, 60)
        salary = random.randint(20000, 80000)
        salary = salary + (salary * 0.05)
        employees.append([name, age, round(salary, 2)])

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Salary(+5%)"])
    writer.writerows(employees)

print("\nCSV file saved successfully")

def generate_pdf(emp_name):
    for emp in employees:
        if emp[0].lower() == emp_name.lower():
            doc = SimpleDocTemplate(f"{emp_name}.pdf")
            styles = getSampleStyleSheet()
            content = []

            content.append(Paragraph("Employee Details", styles["Title"]))
            content.append(Spacer(1, 12))
            content.append(Paragraph(f"Name: {emp[0]}", styles["Normal"]))
            content.append(Paragraph(f"Age: {emp[1]}", styles["Normal"]))
            content.append(Paragraph(f"Salary (+5%): {emp[2]}", styles["Normal"]))

            doc.build(content)
            print(f"{emp_name}.pdf generated successfully")
            return

    print("Employee not found")

while True:
    ask = input("\nGenerate PDF? (yes/no): ").lower()

    if ask in ["yes", "y"]:
        name = input("Enter employee name: ")
        generate_pdf(name)
    elif ask in ["no", "n"]:
        break
    else:
        print("Enter valid input")