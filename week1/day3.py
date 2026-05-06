# Day 3 - OOP and Classes
# Nonhle Maseko

jobs = [
    {"title": "Data Engineer",  "company": "Discovery",     "salary": 550000, "province": "Gauteng"},
    {"title": "Data Analyst",   "company": "Standard Bank", "salary": 420000, "province": "Gauteng"},
    {"title": "BI Developer",   "company": "MTN",           "salary": 480000, "province": "Gauteng"},
    {"title": "Data Scientist", "company": "Nedbank",       "salary": 700000, "province": "Western Cape"},
    {"title": "ML Engineer",    "company": "Takealot",      "salary": 800000, "province": "Western Cape"},
]

class SAJobsAnalyser:

    def __init__(self, jobs):
        self.jobs = jobs
        print(f"Analyser created with {len(self.jobs)} jobs")

    def print_all_jobs(self):
        print("\n--- All Jobs ---")
        for job in self.jobs:
            print(f"{job['title']} at {job['company']} — R{job['salary']:,}")

    def filter_by_province(self, province):
        print(f"\n--- {province} Jobs ---")
        for job in self.jobs:
            if job["province"] == province:
                print(f"{job['title']} at {job['company']} — R{job['salary']:,}")

    def average_salary(self):
        total = 0
        for job in self.jobs:
            total = total + job["salary"]
        return total / len(self.jobs)

    def highest_paying_job(self):
        best_job = None
        best_salary = 0
        for job in self.jobs:
            if job["salary"] > best_salary:
                best_salary = job["salary"]
                best_job = job
        return best_job

analyser = SAJobsAnalyser(jobs)
analyser.print_all_jobs()
analyser.filter_by_province("Gauteng")
analyser.filter_by_province("Western Cape")
avg = analyser.average_salary()
print(f"\nAverage salary: R{avg:,.0f}")
best = analyser.highest_paying_job()
print(f"Highest paying: {best['title']} at {best['company']} — R{best['salary']:,}")
