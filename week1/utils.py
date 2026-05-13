import json

def safe_salary_convert(salary):
    try:
        salary = salary.replace("R", "")
        salary = salary.replace(",", "")
        result = float(salary)
        return result
    except ValueError:
        print(f"Error: cannot convert {salary} number")
        return None
    
def load_jobs(filepath):
    try:
        with open(filepath, "r") as f:
           data = json.load(f)
        return data
    except FileNotFoundError:
        print("Error: file not found")
        return [] 