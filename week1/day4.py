# Day 4 — Error Handling and File I/O
# Nonhle Maseko

def safe_divide(a, b):
    try:
        result = a // b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
def safe_salary_convert(salary):
    try:
        salary = salary.replace("R", "")
        salary = salary.replace(",", "")
        result = float(salary)
        return result
    except ValueError:
        print("Error : not a valid salary")
        return None

print(safe_divide(100, 4))
print(safe_divide(100, 0))
print("##########################")
print(safe_salary_convert("R45,000"))
print(safe_salary_convert("R800,000"))
print(safe_salary_convert("unknown"))

print("##########################")

import json

#writing a JSON file

jobs = [{"title": "Data Engineer", "company": "Discovery",     "salary": 550000},
    {"title": "Data Analyst",   "company": "Standard Bank", "salary": 420000},
    {"title": "ML Engineer",    "company": "Takealot",      "salary": 800000},]

with open("/Users/nonhlemaseko/dev/my-portfolio/week1/sa_jobs.json", "w") as f:
    json.dump(jobs, f, indent=2)

print("File written successfully")