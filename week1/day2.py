#Day 2 - Functions
#Nonhle Maseko

jobs = [{"title": "Data Engineer", "company": "Discovery", "salary": 550000, "province": "Gauteng"},
        {"title": "Data Analyst", "company": "Standard Bank", "salary": 420000, "province": "Gauteng"},
        {"title": "BI Developer", "company": "MTN", "salary": 480000, "province": "Gauteng"},
        {"title": "Data Scientist", "company": "Nedbank", "salary": 700000, "province": "Western Cape"},
        {"title": "ML Engineer", "company": "Takealot", "salary": 800000, "province": "Western Cape"},]

def print_all_jobs(jobs):
    print("\n--- All Jobs ---")
    for job in jobs:
        print(f"{job['title']} at {job['company']}- R{job['salary']:,}")

print_all_jobs(jobs)

#SOLO TASK


def filter_by_province(jobs, province):
    print(f"\n--- {province} Jobs ---")
    for job in jobs:
        if job["province"] == province:
            print(f"{job['title']} at {job['company']} - R{job['salary']:,} ")

filter_by_province(jobs, "Gauteng")
filter_by_province(jobs, "Western Cape")

#AVERAGE SALARY

def average_salary(jobs):
    print("\n--- Average Salary ----")

    salary = 0
    for job in jobs:
        salary = salary + job["salary"] 
    avg = salary/len(jobs)
    return avg

avg = average_salary(jobs)
print(f"Average salary: R{avg:,.0f}")


#HIGHEST PAYING JOB


def highest_paying_job(jobs):
    print("\n--- Highest paying job ---")
    current_highest = 0
    current_job = None
    for job in jobs:
        if job["salary"] > current_highest:
            current_highest = job["salary"]
            current_job = job
    return current_job

best = highest_paying_job(jobs)
print(f"Highest paying: {best['title']}  at {best['company']} - R{best['salary']:,}")