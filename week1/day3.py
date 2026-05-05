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

analyser = SAJobsAnalyser(jobs)
analyser.print_all_jobs()
