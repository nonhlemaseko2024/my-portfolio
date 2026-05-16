#main.py - runs everything
# Nonhle Maseko

from analyser import SAJobsAnalyser
from utils import load_jobs

jobs = load_jobs("/Users/nonhlemaseko/dev/my-portfolio/week1/sa_jobs.json")


analyser = SAJobsAnalyser(jobs)
analyser.print_all_jobs()
analyser.filter_by_province("Gauteng")
avg = analyser.average_salary()
print(f"\nAverage salary: R{avg:,.0f}")
best = analyser.highest_paying_job()
print(f"Highest paying: {best['title']} at {best['company']} — R{best['salary']:,}")

