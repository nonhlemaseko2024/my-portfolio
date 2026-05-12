# Day 4 — Error Handling and File I/O
# Nonhle Maseko

import json

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
        print("Error: not a valid salary")
        return None

jobs = [
    {"title": "Data Engineer", "company": "Discovery",     "salary": 550000},
    {"title": "Data Analyst",  "company": "Standard Bank", "salary": 420000},
    {"title": "ML Engineer",   "company": "Takealot",      "salary": 800000},
]

with open("/Users/nonhlemaseko/dev/my-portfolio/week1/sa_jobs.json", "w") as f:
    json.dump(jobs, f, indent=2)
print("File written successfully")

def load_jobs(filepath):
    try:
        with open(filepath, "r") as f:
            jobs_loaded = json.load(f)
        return jobs_loaded
    except FileNotFoundError:
        print("Error: File not found")
        return []

jobs_loaded = load_jobs("/Users/nonhlemaseko/dev/my-portfolio/week1/sa_jobs.json")
for job in jobs_loaded:
    print(f"{job['title']} at {job['company']} — R{job['salary']:,}")
