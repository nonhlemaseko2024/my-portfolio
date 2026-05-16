# analyser.py — SAJobsAnalyser class
# Nonhle Maseko

from utils import safe_salary_convert, load_jobs

class SAJobsAnalyser:

    def __init__(self, jobs):
        self.jobs = jobs
        print(f"Analyser created with {len(self.jobs)} jobs")

    def print_all_jobs(self):
        print("\n--- All Jobs ---")
        for job in self.jobs:
            print(f"{job['title']} at {job['company']} - R{job['salary']:,}")

    def filter_by_province(self, province):
        print(f"\n--- {province} Jobs ---")
        for job in self.jobs:
            if job["province"] == province:
                print(f"{job['title']} at {job['company']} - R{job['salary']:,}")

    def average_salary(self):
        total = 0
        for job in self.jobs:
            total = total + job["salary"]
        avg = total / len(self.jobs)
        return avg

    def highest_paying_job(self):
        best_job = None
        best_salary = 0
        for job in self.jobs:
            if job["salary"] > best_salary:
                best_salary = job["salary"]
                best_job = job
        return best_job
