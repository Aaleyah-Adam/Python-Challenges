from datetime import datetime

start_date = datetime.strptime(input("Enter the project start date (YYYY-MM-DD): "), "%Y-%m-%d")
end_date = datetime.strptime(input("Enter the project end date (YYYY-MM-DD): "), "%Y-%m-%d")

duration = (end_date - start_date).days
print(f"The project duration is {duration} days.")# Write your code here :-)
